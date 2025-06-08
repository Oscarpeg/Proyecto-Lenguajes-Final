import sys
import random
sys.path.append('./generated')

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from DeepLearningDSLLexer import DeepLearningDSLLexer
from DeepLearningDSLParser import DeepLearningDSLParser
from DeepLearningDSLVisitor import DeepLearningDSLVisitor as DeepLearningDSLBaseVisitor
from arithmetic_engine import ArithmeticEngine
from matrix_engine import MatrixEngine
from ml_engine import LinearRegressionEngine, MLPClassifierEngine, NeuralNetworkEngine
from file_manager import FileManager
from plotter import Plotter
from kmeans_engine import KMeansEngine
from autoencoder_engine import AutoencoderEngine



class DSLInterpreter(DeepLearningDSLBaseVisitor):
    def __init__(self):
        # Symbol tables
        self.variables = {}
        self.functions = {}
        
        # Engines
        self.arithmetic = ArithmeticEngine()
        self.matrix = MatrixEngine()
        self.linear_reg = LinearRegressionEngine()
        self.mlp = MLPClassifierEngine()
        self.neural_net = NeuralNetworkEngine()
        self.file_manager = FileManager()
        self.plotter = Plotter()
        self.kmeans = KMeansEngine(n_clusters=2) # Default value, will be overridden by KMEANS call
        self.autoencoder = AutoencoderEngine(input_dim=2, encoding_dim=1) # Default, will be overridden
        
        # Flag for return values
        self.return_value = None
        self.in_function = False
    
    def visitProgram(self, ctx):
        """Visit the main program"""
        return self.visit(ctx.statement_list())
    
    def visitStatement_list(self, ctx):
        """Visit a list of statements"""
        if ctx.statement():
            # Visit first statement
            result = self.visit(ctx.statement())
            
            # If there's a return in function, stop executing
            if self.return_value is not None and self.in_function:
                return self.return_value
                
            # Visit rest of statements
            if ctx.statement_list():
                rest_result = self.visit(ctx.statement_list())
                return rest_result if rest_result is not None else result
        return None
    
    def visitStatement(self, ctx):
        """Visit a single statement"""
        if ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.conditional():
            return self.visit(ctx.conditional())
        elif ctx.loop():
            return self.visit(ctx.loop())
        elif ctx.function_def():
            return self.visit(ctx.function_def())
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        elif ctx.expression():
            return self.visit(ctx.expression())
        return None
    
    def visitAssignment(self, ctx):
        """Handle variable assignment"""
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value
        return value
    
    def visitExpression(self, ctx):
        """Evaluate expressions with precedence"""
        term_value = self.visit(ctx.term())
        return self.visit_expr_rest(ctx.expr_rest(), term_value)
    
    def visit_expr_rest(self, ctx, left_value):
        """Handle expression rest (+ and - operations)"""
        if not ctx:
            return left_value
            
        if ctx.PLUS():
            right_value = self.visit(ctx.term())
            result = self.arithmetic.add(left_value, right_value)
            return self.visit_expr_rest(ctx.expr_rest(), result)
        elif ctx.MINUS():
            right_value = self.visit(ctx.term())
            result = self.arithmetic.subtract(left_value, right_value)
            return self.visit_expr_rest(ctx.expr_rest(), result)
        else:
            return left_value
    
    def visitTerm(self, ctx):
        """Evaluate terms (*, /, % operations)"""
        factor_value = self.visit(ctx.factor())
        return self.visit_term_rest(ctx.term_rest(), factor_value)
    
    def visit_term_rest(self, ctx, left_value):
        """Handle term rest (*, /, % operations)"""
        if not ctx:
            return left_value
            
        if ctx.MULT():
            right_value = self.visit(ctx.factor())
            result = self.arithmetic.multiply(left_value, right_value)
            return self.visit_term_rest(ctx.term_rest(), result)
        elif ctx.DIV():
            right_value = self.visit(ctx.factor())
            result = self.arithmetic.divide(left_value, right_value)
            return self.visit_term_rest(ctx.term_rest(), result)
        elif ctx.MOD():
            right_value = self.visit(ctx.factor())
            result = self.arithmetic.modulo(left_value, right_value)
            return self.visit_term_rest(ctx.term_rest(), result)
        else:
            return left_value
    
    def visitFactor(self, ctx):
        """Evaluate factors (^ operations)"""
        base_value = self.visit(ctx.base())
        return self.visit_factor_rest(ctx.factor_rest(), base_value)
    
    def visit_factor_rest(self, ctx, left_value):
        """Handle factor rest (^ operation)"""
        if not ctx:
            return left_value
            
        if ctx.POWER():
            right_value = self.visit(ctx.base())
            result = self.arithmetic.power(left_value, right_value)
            return self.visit_factor_rest(ctx.factor_rest(), result)
        else:
            return left_value
    
    def visitBase(self, ctx):
        """Evaluate base expressions"""
        if ctx.ID():
            var_name = ctx.ID().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                raise NameError(f"Variable '{var_name}' not defined")
        elif ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        elif ctx.STRING():
            # Remove quotes
            return ctx.STRING().getText()[1:-1]
        elif ctx.expression():
            # Parenthesized expression
            return self.visit(ctx.expression())
        elif ctx.list_or_matrix_expr():
            return self.visit(ctx.list_or_matrix_expr())
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        elif ctx.unary_expr():
            return self.visit(ctx.unary_expr())
        return None
    
    def visitUnary_expr(self, ctx):
        """Handle unary expressions"""
        if ctx.MINUS():
            value = self.visit(ctx.base())
            return self.arithmetic.negate(value)
        elif ctx.trig_func():
            func_name = ctx.trig_func().getText()
            value = self.visit(ctx.expression())
            return self.arithmetic.trigonometric(func_name, value)
        return None
    
    def visitList_or_matrix_expr(self, ctx):
        """Handle list or matrix expressions with auto-detection"""
        if ctx.list_or_matrix_content():
            return self.visit(ctx.list_or_matrix_content())
        elif ctx.matrix_operation():
            return self.visit(ctx.matrix_operation())
        return []
    
    def visitList_or_matrix_content(self, ctx):
        """Build list or matrix with auto-detection"""
        if not ctx.list_or_matrix_row():
            return []  # Empty list
        
        elements = []
        
        # Get first element/row
        first_element = self.visit(ctx.list_or_matrix_row())
        elements.append(first_element)
        
        # Get rest of elements/rows
        if ctx.list_or_matrix_content_rest():
            rest_elements = self.visit_list_or_matrix_content_rest(ctx.list_or_matrix_content_rest())
            elements.extend(rest_elements)
        
        # AUTO-DETECTION:
        # If all elements are primitives (int, float, str), return simple list
        # If any element is a list, return matrix
        
        if all(isinstance(elem, (int, float, str, bool)) for elem in elements):
            # Simple list: [1, 2, 3, "hello"]
            return elements
        elif all(isinstance(elem, list) for elem in elements):
            # Matrix: [[1, 2], [3, 4]]
            return self.matrix.create_matrix(elements)
        else:
            # Mixed types - treat as simple list
            return elements
    
    def visit_list_or_matrix_content_rest(self, ctx):
        """Get remaining elements/rows"""
        if not ctx or not ctx.list_or_matrix_row():
            return []
        
        elements = []
        element = self.visit(ctx.list_or_matrix_row())
        elements.append(element)
        
        if ctx.list_or_matrix_content_rest():
            rest_elements = self.visit_list_or_matrix_content_rest(ctx.list_or_matrix_content_rest())
            elements.extend(rest_elements)
        
        return elements
    
    def visitList_or_matrix_row(self, ctx):
        """Handle a single row/element"""
        if ctx.expression_list():
            # Matrix row: [1, 2, 3]
            return self.visit(ctx.expression_list())
        elif ctx.expression():
            # Simple element: 1, "hello", variable
            return self.visit(ctx.expression())
        return None
    
    def visitExpression_list(self, ctx):
        """Build list of expressions"""
        elements = []
        # Get first expression
        first_expr = self.visit(ctx.expression())
        elements.append(first_expr)
        
        # Get rest of expressions
        rest_elements = self.visit_expression_list_rest(ctx.expression_list_rest())
        elements.extend(rest_elements)
        
        return elements
    
    def visit_expression_list_rest(self, ctx):
        """Get remaining expressions"""
        if not ctx or not ctx.expression():
            return []
        
        elements = []
        expr = self.visit(ctx.expression())
        elements.append(expr)
        
        if ctx.expression_list_rest():
            rest_elements = self.visit_expression_list_rest(ctx.expression_list_rest())
            elements.extend(rest_elements)
        
        return elements
    
    def visitMatrix_operation(self, ctx):
        """Handle matrix operations"""
        try:
            if ctx.TRANSPOSE():
                matrix = self.visit(ctx.expression(0))
                return self.matrix.transpose(matrix)
                
            elif ctx.INVERSE():
                matrix = self.visit(ctx.expression(0))
                return self.matrix.inverse(matrix)
                
            elif ctx.MATMULT():
                matrix1 = self.visit(ctx.expression(0))
                matrix2 = self.visit(ctx.expression(1))
                return self.matrix.multiply(matrix1, matrix2)
                
            elif ctx.MATADD():
                matrix1 = self.visit(ctx.expression(0))
                matrix2 = self.visit(ctx.expression(1))
                return self.matrix.add(matrix1, matrix2)
                
            elif ctx.MATSUB():
                matrix1 = self.visit(ctx.expression(0))
                matrix2 = self.visit(ctx.expression(1))
                return self.matrix.subtract(matrix1, matrix2)
                
        except Exception as e:
            raise RuntimeError(f"Matrix operation error: {str(e)}")
        
        return None
    
    def visitConditional(self, ctx):
        """Handle if-else statements"""
        condition_value = self.visit(ctx.condition())
        
        if self.is_truthy(condition_value):
            return self.visit(ctx.statement_list())
        elif ctx.else_part() and ctx.else_part().statement_list():
            return self.visit(ctx.else_part().statement_list())
        return None
    
    def visitCondition(self, ctx):
        """Evaluate conditions"""
        if ctx.rel_op():
            # Relational operation
            left_value = self.visit(ctx.expression(0))
            right_value = self.visit(ctx.expression(1))
            operator = ctx.rel_op().getText()
            return self.arithmetic.compare(left_value, right_value, operator)
        else:
            # Single expression
            return self.visit(ctx.expression(0))
    
    def visitFor_loop(self, ctx):
        """Handle for loops"""
        # Initialize
        self.visit(ctx.assignment(0))
        
        results = []
        while True:
            # Check condition
            condition_value = self.visit(ctx.condition())
            if not self.is_truthy(condition_value):
                break
            
            # Execute body
            result = self.visit(ctx.statement_list())
            if result is not None:
                results.append(result)
            
            # Update
            self.visit(ctx.assignment(1))
        
        return results[-1] if results else None
    
    def visitWhile_loop(self, ctx):
        """Handle while loops"""
        results = []
        while True:
            # Check condition
            condition_value = self.visit(ctx.condition())
            if not self.is_truthy(condition_value):
                break
            
            # Execute body
            result = self.visit(ctx.statement_list())
            if result is not None:
                results.append(result)
        
        return results[-1] if results else None
    
    def visitFunction_def(self, ctx):
        """Define a function"""
        func_name = ctx.ID().getText()
        params = self.visit(ctx.param_list()) if ctx.param_list() else []
        body = ctx.statement_list()
        return_stmt = ctx.return_stmt()
        
        self.functions[func_name] = {
            'params': params,
            'body': body,
            'return_stmt': return_stmt
        }
        return None
    
    def visitParam_list(self, ctx):
        """Get function parameters"""
        if not ctx.ID():
            return []
        
        params = [ctx.ID().getText()]
        if ctx.param_list_rest():
            rest_params = self.visit_param_list_rest(ctx.param_list_rest())
            params.extend(rest_params)
        
        return params
    
    def visit_param_list_rest(self, ctx):
        """Get remaining parameters"""
        if not ctx or not ctx.ID():
            return []
        
        params = [ctx.ID().getText()]
        if ctx.param_list_rest():
            rest_params = self.visit_param_list_rest(ctx.param_list_rest())
            params.extend(rest_params)
        
        return params
    
    def visitReturn_stmt(self, ctx):
        """Handle return statement"""
        self.return_value = self.visit(ctx.expression())
        return self.return_value
    
    def visitFunction_call(self, ctx):
        """Handle function calls"""
        if ctx.ID():
            # Llamada de función de usuario
            func_name = ctx.ID().getText()
            args = self.visit(ctx.arg_list()) if ctx.arg_list() else []
            return self.call_user_function(func_name, args)
        elif ctx.ml_function():
            return self.visit(ctx.ml_function())
        elif ctx.io_function():
            return self.visit(ctx.io_function())
        elif ctx.plot_function():
            return self.visit(ctx.plot_function())
        return None
    
    def visitArg_list(self, ctx):
        """Get function arguments"""
        if not ctx.expression():
            return []
        
        args = [self.visit(ctx.expression())]
        if ctx.arg_list_rest():
            rest_args = self.visit_arg_list_rest(ctx.arg_list_rest())
            args.extend(rest_args)
        
        return args
    
    def visit_arg_list_rest(self, ctx):
        """Get remaining arguments"""
        if not ctx or not ctx.expression():
            return []
        
        args = [self.visit(ctx.expression())]
        if ctx.arg_list_rest():
            rest_args = self.visit_arg_list_rest(ctx.arg_list_rest())
            args.extend(rest_args)
        
        return args
    
    def visitMl_function(self, ctx):
        """Handle ML function calls"""
        if ctx.LINEAR_REGRESSION():
            X = self.visit(ctx.expression(0))
            y = self.visit(ctx.expression(1))
            
            # Create a new linear regression model and fit it
            model = self.linear_reg.__class__()  # Create new instance
            return model.fit(X, y)
            
        elif ctx.MLP_CLASSIFIER():
            X = self.visit(ctx.expression(0))
            y = self.visit(ctx.expression(1))
            hidden_size = self.visit(ctx.expression(2))
            
            # Create a new MLP classifier model and fit it
            model = self.mlp.__class__(hidden_size=hidden_size)
            return model.fit(X, y)
            
        elif ctx.NEURAL_NETWORK():
            X = self.visit(ctx.expression(0))
            y = self.visit(ctx.expression(1))
            architecture = self.visit(ctx.expression(2))
            
            # Create a new neural network model
            model = self.neural_net.__class__(architecture=architecture)
            return model.fit(X, y)
            
        elif ctx.PREDICT():
            model = self.visit(ctx.expression(0))
            X = self.visit(ctx.expression(1))
            
            # Check if model has predict method
            if hasattr(model, 'predict'):
                return model.predict(X)
            else:
                raise ValueError("Object does not have predict method")
                
        elif ctx.TRAIN():
            model = self.visit(ctx.expression(0))
            data = self.visit(ctx.expression(1))
            
            # Check if model has train method, or use fit
            if hasattr(model, 'train'):
                return model.train(data)
            elif hasattr(model, 'fit'):
                # Assume data is [X, y] format
                if isinstance(data, list) and len(data) == 2:
                    return model.fit(data[0], data[1])
                else:
                    raise ValueError("Train data must be [X, y] format")
            else:
                raise ValueError("Object does not have train or fit method")
        
        # ===== K-MEANS FUNCTIONS =====
        
        elif ctx.KMEANS():
            X = self.visit(ctx.expression(0))
            n_clusters = self.visit(ctx.expression(1))
            
            # Create a new K-Means model and fit it
            model = KMeansEngine(n_clusters=n_clusters)
            return model.fit(X)
        
        elif ctx.FIT_PREDICT():
            model = self.visit(ctx.expression(0))
            X = self.visit(ctx.expression(1))
            
            # Check if model has fit_predict method
            if hasattr(model, 'fit_predict'):
                return model.fit_predict(X)
            else:
                raise ValueError("Object does not have fit_predict method")
        
        elif ctx.GET_CENTROIDS():
            model = self.visit(ctx.expression(0))
            
            # Check if model has get_centroids method
            if hasattr(model, 'get_centroids'):
                return model.get_centroids()
            else:
                raise ValueError("Object does not have get_centroids method")
        
        # ===== AUTOENCODER FUNCTIONS =====
        
        elif ctx.AUTOENCODER():
            X = self.visit(ctx.expression(0))
            encoding_dim = self.visit(ctx.expression(1))
            
            # Determinar input_dim automáticamente
            if X and isinstance(X[0], list):
                input_dim = len(X[0])  # Matriz: usar longitud de la primera fila
            elif X:
                input_dim = len(X)     # Lista: usar longitud total
            else:
                input_dim = 2          # Default si no hay datos
            
            # Create and train autoencoder
            model = AutoencoderEngine(input_dim=input_dim, encoding_dim=encoding_dim)
            return model.fit(X)
        
        elif ctx.ENCODE():
            model = self.visit(ctx.expression(0))
            X = self.visit(ctx.expression(1))
            
            # Check if model has encode method
            if hasattr(model, 'encode'):
                return model.encode(X)
            else:
                raise ValueError("Object does not have encode method")
        
        elif ctx.DECODE():
            model = self.visit(ctx.expression(0))
            encoded_X = self.visit(ctx.expression(1))
            
            # Check if model has decode method
            if hasattr(model, 'decode'):
                return model.decode(encoded_X)
            else:
                raise ValueError("Object does not have decode method")
        
        elif ctx.RECONSTRUCT():
            model = self.visit(ctx.expression(0))
            X = self.visit(ctx.expression(1))
            
            # Check if model has reconstruct method
            if hasattr(model, 'reconstruct'):
                return model.reconstruct(X)
            else:
                raise ValueError("Object does not have reconstruct method")
        
        elif ctx.RECONSTRUCTION_ERROR():
            model = self.visit(ctx.expression(0))
            X = self.visit(ctx.expression(1))
            
            # Check if model has reconstruction_error method
            if hasattr(model, 'reconstruction_error'):
                return model.reconstruction_error(X)
            else:
                raise ValueError("Object does not have reconstruction_error method")
        
        return None
    
    def visitIo_function(self, ctx):
        """Handle IO function calls"""
        if ctx.READ_FILE():
            filename = ctx.STRING().getText()[1:-1]  # Remove quotes
            return self.file_manager.read_file(filename)
        elif ctx.WRITE_FILE():
            filename = ctx.STRING().getText()[1:-1]  # Remove quotes
            content = self.visit(ctx.expression())
            return self.file_manager.write_file(filename, content)
        elif ctx.PRINT():
            value = self.visit(ctx.expression())
            return self.file_manager.print_value(value)
        return None
    
    def visitPlot_function(self, ctx):
        """Handle plot function calls"""
        try:
            if ctx.PLOT():
                data = self.visit(ctx.expression(0))
                return self.plotter.plot(data)
                
            elif ctx.SCATTER():
                x_data = self.visit(ctx.expression(0))
                y_data = self.visit(ctx.expression(1))
                return self.plotter.scatter(x_data, y_data)
                
            elif ctx.HISTOGRAM():
                data = self.visit(ctx.expression(0))
                return self.plotter.histogram(data)
                
        except Exception as e:
            error_msg = f"Plot function error: {str(e)}"
            return error_msg
        
        return None
    
    def call_user_function(self, func_name, args):
        """Call a user-defined function"""
        if func_name not in self.functions:
            raise NameError(f"Function '{func_name}' not defined")
        
        func_def = self.functions[func_name]
        params = func_def['params']
        
        if len(args) != len(params):
            raise ValueError(f"Function '{func_name}' expects {len(params)} arguments, got {len(args)}")
        
        # Save current state
        old_variables = self.variables.copy()
        old_in_function = self.in_function
        old_return_value = self.return_value
        
        # Set up function context
        self.in_function = True
        self.return_value = None
        
        # Bind arguments to parameters
        for param, arg in zip(params, args):
            self.variables[param] = arg
        
        try:
            # Execute function body
            self.visit(func_def['body'])
            
            # Execute return statement
            result = self.visit(func_def['return_stmt'])
            
            return result
        finally:
            # Restore state
            self.variables = old_variables
            self.in_function = old_in_function
            self.return_value = old_return_value
    
    def is_truthy(self, value):
        """Check if value is truthy"""
        if isinstance(value, bool):
            return value
        elif isinstance(value, (int, float)):
            return value != 0
        elif isinstance(value, str):
            return len(value) > 0
        elif isinstance(value, list):
            return len(value) > 0
        else:
            return value is not None


# Error listener for custom error handling
class DSLErrorListener(ErrorListener):
    def __init__(self):
        super(DSLErrorListener, self).__init__()
        self.errors = []
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"Syntax error at line {line}, column {column}: {msg}"
        self.errors.append(error_msg)
    
    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass  # Silenciar ambigüedades
    
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass  # Silenciar
    
    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass  # Silenciar


def interpret_code(code):
    """Main function to interpret DSL code"""
    try:
        # Create input stream
        input_stream = InputStream(code)
        
        # Create lexer
        lexer = DeepLearningDSLLexer(input_stream)
        
        # Create token stream
        token_stream = CommonTokenStream(lexer)
        
        # Create parser
        parser = DeepLearningDSLParser(token_stream)
        
        # Add error listener
        error_listener = DSLErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        
        # Parse the program
        tree = parser.program()
        
        # Check for syntax errors
        if error_listener.errors:
            return None, error_listener.errors
        
        # Create interpreter and visit the tree
        interpreter = DSLInterpreter()
        result = interpreter.visit(tree)
        
        return result, []
        
    except Exception as e:
        return None, [str(e)]


if __name__ == "__main__":
    # Example usage
    code = """
    x = 5;
    y = 3;
    z = x + y * 2;
    print(z);
    
    matrix1 = [[1, 2], [3, 4]];
    matrix2 = [[5, 6], [7, 8]];
    result = matmult(matrix1, matrix2);
    print(result);
    """
    
    result, errors = interpret_code(code)
    
    if errors:
        print("Errors found:")
        for error in errors:
            print(f"  {error}")
    else:
        print(f"Program executed successfully. Result: {result}")