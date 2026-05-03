import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")

# ---------------- DB CONNECTION ----------------
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# ---------------- CLEAR OLD DATA ----------------
cursor.execute("TRUNCATE questions, subtopics, topics RESTART IDENTITY CASCADE")

# ---------------- INSERT TOPICS ----------------
topics = ['Python', 'SQL', 'DSA', 'Machine Learning', 'Statistics', 'Data Analysis']

cursor.executemany(
    "INSERT INTO topics (name) VALUES (%s) ON CONFLICT DO NOTHING",
    [(t,) for t in topics]
)

# ---------------- HELPERS ----------------
def get_topic_id(name):
    cursor.execute("SELECT id FROM topics WHERE name = %s", (name,))
    row = cursor.fetchone()
    if not row:
        raise ValueError(f"Topic not found: {name}")
    return row[0]

def get_subtopic_id(topic_id, name):
    cursor.execute(
        "SELECT id FROM subtopics WHERE topic_id = %s AND name = %s",
        (topic_id, name)
    )
    row = cursor.fetchone()
    if not row:
        raise ValueError(f"Subtopic not found: {name}")
    return row[0]

# ---------------- GET TOPIC IDs ----------------
python_id = get_topic_id('Python')
sql_id = get_topic_id('SQL')
dsa_id = get_topic_id('DSA')
ml_id = get_topic_id('Machine Learning')
stats_id = get_topic_id('Statistics')
da_id = get_topic_id('Data Analysis')

# ---------------- INSERT SUBTOPICS ----------------
subtopics = [
    # Python
    (python_id, 'Python Basics'),
    (python_id, 'OOP'),
    (python_id, 'Functions'),
    (python_id, 'Decorators'),
    (python_id, 'Generators'),
    (python_id, 'NumPy'),
    (python_id, 'Pandas'),
    (python_id, 'Python DSA Patterns'),

    # SQL
    (sql_id, 'Joins'),
    (sql_id, 'Basic Queries'),
    (sql_id, 'Window Functions'),
    (sql_id, 'CTE'),
    (sql_id, 'Indexing'),
    (sql_id, 'Query Optimization'),

    # DSA
    (dsa_id, 'Arrays'),
    (dsa_id, 'Hashing'),
    (dsa_id, 'Sliding Window'),
    (dsa_id, 'Two Pointers'),
    (dsa_id, 'Stack & Queue'),
    (dsa_id, 'Trees'),
    (dsa_id, 'Graphs (Basic)'),

    # Machine Learning
    (ml_id, 'ML Basics'),
    (ml_id, 'Algorithms'),
    (ml_id, 'Metrics'),
    (ml_id, 'Feature Engineering'),
    (ml_id, 'Pipelines'),
    (ml_id, 'Model Evaluation'),

    # Statistics
    (stats_id, 'Probability'),
    (stats_id, 'Distributions'),
    (stats_id, 'Hypothesis Testing'),
    (stats_id, 'A/B Testing'),

    # Data Analysis
    (da_id, 'Pandas'),
    (da_id, 'Data Cleaning'),
    (da_id, 'EDA'),
    (da_id, 'Visualization'),
    (da_id, 'Business Case Studies'),
]

cursor.executemany(
    "INSERT INTO subtopics (topic_id, name) VALUES (%s, %s) ON CONFLICT DO NOTHING",
    subtopics
)

# ---------------- GET SUBTOPIC IDs (FIXED) ----------------
python_basics_id = get_subtopic_id(python_id, 'Python Basics')
oop_id = get_subtopic_id(python_id, 'OOP')
functions_id = get_subtopic_id(python_id, 'Functions')
decorators_id = get_subtopic_id(python_id, 'Decorators')
generators_id = get_subtopic_id(python_id, 'Generators')
numpy_id = get_subtopic_id(python_id, 'NumPy')
pandas_id = get_subtopic_id(python_id, 'Pandas')
dsa_patterns_id = get_subtopic_id(python_id, 'Python DSA Patterns')

sql_joins_id = get_subtopic_id(sql_id, 'Joins')
sql_basic_id = get_subtopic_id(sql_id, 'Basic Queries')
sql_window_id = get_subtopic_id(sql_id, 'Window Functions')
sql_cte_id = get_subtopic_id(sql_id, 'CTE')
sql_indexing_id = get_subtopic_id(sql_id, 'Indexing')
sql_optimization_id = get_subtopic_id(sql_id, 'Query Optimization')


arrays_id = get_subtopic_id(dsa_id, 'Arrays')
hashing_id = get_subtopic_id(dsa_id, 'Hashing')
sliding_window_id = get_subtopic_id(dsa_id, 'Sliding Window')
two_pointers_id = get_subtopic_id(dsa_id, 'Two Pointers')
stack_queue_id = get_subtopic_id(dsa_id, 'Stack & Queue')
trees_id = get_subtopic_id(dsa_id, 'Trees')
graphs_id = get_subtopic_id(dsa_id, 'Graphs (Basic)')

ml_basics_id = get_subtopic_id(ml_id, 'ML Basics')
ml_algorithms_id = get_subtopic_id(ml_id, 'Algorithms')
ml_metrics_id = get_subtopic_id(ml_id, 'Metrics')
ml_feature_eng_id = get_subtopic_id(ml_id, 'Feature Engineering')
ml_pipelines_id = get_subtopic_id(ml_id, 'Pipelines')
ml_model_eval_id = get_subtopic_id(ml_id, 'Model Evaluation')

probability_id = get_subtopic_id(stats_id, 'Probability')
distributions_id = get_subtopic_id(stats_id, 'Distributions')
hypothesis_testing_id = get_subtopic_id(stats_id, 'Hypothesis Testing')
ab_testing_id = get_subtopic_id(stats_id, 'A/B Testing')

pandas_da_id = get_subtopic_id(da_id, 'Pandas')
data_cleaning_id = get_subtopic_id(da_id, 'Data Cleaning')
eda_id = get_subtopic_id(da_id, 'EDA')
visualization_id = get_subtopic_id(da_id, 'Visualization')
business_case_id = get_subtopic_id(da_id, 'Business Case Studies')

questions = [
# ── PYTHON BASICS ──
(python_id, python_basics_id, "easy", "What is Python?","Compiled language","High-level programming language","Assembly language","Hardware language","b","Python is a high-level, interpreted programming language known for simplicity and readability.","basics"),
(python_id, python_basics_id, "easy", "Which symbol is used for comments in Python?","//","/*","#","--","c","In Python, the # symbol is used to write single-line comments.","basics"),
(python_id, python_basics_id, "easy", "What is the output of print(type(10))?","<class 'float'>","<class 'int'>","<class 'str'>","<class 'num'>","b","10 is an integer in Python, so type() returns <class 'int'>.","basics"),
(python_id, python_basics_id, "easy", "Which of these is a mutable data type?","Tuple","String","List","Integer","c","Lists are mutable in Python — you can change their elements after creation.","basics"),
(python_id, python_basics_id, "easy", "What does len() do?","Deletes a list","Returns length of object","Converts to integer","Sorts a list","b","len() returns the number of items in an object like a list, string, or tuple.","basics"),
(python_id, python_basics_id, "easy", "How do you create a variable in Python?","var x=5","int x=5","x=5","$x=5","c","Python uses dynamic typing — just write x=5 to create a variable.","basics"),
(python_id, python_basics_id, "easy", "Which keyword is used to create a class?","define","struct","class","object","c","The 'class' keyword is used to define a class in Python.","basics"),
(python_id, python_basics_id, "easy", "What is the correct file extension for Python?",".py",".python",".pt",".p","a","Python files use the .py extension.","basics"),
(python_id, python_basics_id, "easy", "Which function converts string to integer?","str()","float()","int()","num()","c","int() converts a string or float to an integer in Python.","basics"),
(python_id, python_basics_id, "easy", "What is a tuple?","Mutable sequence","Immutable sequence","Key-value pair","Unordered set","b","Tuples are immutable sequences — once created they cannot be changed.","basics"),
(python_id, python_basics_id, "easy", "What does 'import' do in Python?","Creates a function","Loads a module","Deletes a file","Starts a loop","b","import loads external modules or libraries into your Python program.","basics"),
(python_id, python_basics_id, "easy", "What is the output of 2**3?","6","8","9","5","b","** is the power operator in Python. 2**3 = 8.","basics"),
(python_id, python_basics_id, "easy", "Which data type stores key-value pairs?", "List","Tuple","Set","Dictionary","d","Dictionaries store data as key-value pairs in Python.","basics"),
(python_id, python_basics_id, "easy", "What is the output of bool(0)?", "True","False","None","Error","b","0 is falsy in Python, so bool(0) returns False.","basics"),
(python_id, python_basics_id, "easy", "How do you start a for loop in Python?", "for i in range(5):","for(i=0;i<5;i++)","foreach i in 5:","loop i to 5:","a","Python for loops use 'for i in range(n):' syntax.","basics"),
(python_id, python_basics_id, "easy", "What does the 'not' operator do?","Adds values","Reverses boolean","Multiplies","Divides","b","'not' reverses a boolean value.","basics"),
(python_id, python_basics_id, "easy", "Which method adds an item to a list?", "add()","insert()","append()","push()","c","append() adds an item to the end of a list.","basics"),
(python_id, python_basics_id, "easy", "What is slicing in Python?","Deleting elements","Extracting a portion of sequence","Sorting a list","Adding elements","b","Slicing extracts a portion using [start:end].","basics"),
(python_id, python_basics_id, "easy", "What does 'pass' do in Python?","Exits the loop","Does nothing — placeholder","Returns a value","Skips an iteration","b","'pass' is a placeholder statement.","basics"),
(python_id, python_basics_id, "easy", "Which keyword exits a loop?","exit","stop","break","end","c","'break' immediately exits a loop.","basics"),
(python_id, python_basics_id, "medium", "What is id() in Python?","Object value","Memory address identifier","Type checker","Hash value","b","id() returns unique identifier (memory address).","memory"),
(python_id, python_basics_id, "medium", "What is is vs == ?","Same","is checks identity, == checks equality","== faster","is compares value","b","is checks memory identity, == checks value equality.","comparison"),
(python_id, python_basics_id, "medium", "What is shallow copy?","Copies everything","Copies references","Deletes data","Creates new object fully","b","Shallow copy copies references, not nested objects.","memory"),
(python_id, python_basics_id, "medium", "What is deep copy?","Copies reference","Copies nested objects fully","Same as shallow","Deletes original","b","Deep copy recursively copies all objects.","memory"),
(python_id, python_basics_id, "medium", "What is GIL?","Global Interpreter Lock","Memory lock","Thread lock","Process lock","a","GIL ensures only one thread executes Python bytecode.","threads"),
(python_id, python_basics_id, "medium", "Are Python threads truly parallel?","Yes","No due to GIL","Only sometimes","Depends","b","GIL prevents true parallel execution.","threads"),
(python_id, python_basics_id, "easy", "What is list comprehension?","Loop alternative","Dictionary method","Sorting method","Generator","a","Compact syntax for creating lists.","basics"),
(python_id, python_basics_id, "easy", "What is set used for?","Ordered data","Unique elements","Key-value","Mutable tuple","b","Set stores unique unordered elements.","basics"),
(python_id, python_basics_id, "easy", "What is frozenset?","Mutable set","Immutable set","List","Dictionary","b","frozenset is immutable version of set.","basics"),
(python_id, python_basics_id, "medium", "What is duck typing?","Strict typing","Type checking","Behavior-based typing","Compilation","c","If it behaves like a type, it is treated as that type.","concept"),
(python_id, python_basics_id, "medium", "Output? a=[1,2,3]; b=a; b.append(4); print(a)","[1,2,3]","[1,2,3,4]","Error","[4]","b","Same reference → mutation affects both.","lists"),
(python_id, python_basics_id, "medium", "Output? a=[1,2,3]; b=a[:] ; b.append(4); print(a)","[1,2,3,4]","[1,2,3]","Error","None","b","Copy created → original unchanged.","lists"),
(python_id, python_basics_id, "hard", "Output? print(0.1 + 0.2 == 0.3)","True","False","Error","None","b","Floating point precision issue.","edge"),
(python_id, python_basics_id, "easy", "Output? print(bool('False'))","True","False","Error","None","a","Non-empty string is True.","basics"),
(python_id, python_basics_id, "medium", "Output? print([] is [])","True","False","Error","None","b","Different objects in memory.","memory"),
(python_id, python_basics_id, "easy", "Output? print([] == [])","True","False","Error","None","a","Values equal → True.","basics"),

# ── PYTHON OOP ──

(python_id, oop_id, "medium","What will happen if __init__ returns a value?","Object created normally","Error is raised","Value is ignored","Constructor skipped","b","__init__ should not return anything. Returning a value raises TypeError.","oop"),
(python_id, oop_id, "easy","Which method is called when an object is printed?","__repr__","__str__","__print__","__format__","b","__str__ defines human-readable string output for print().","oop"),
(python_id, oop_id, "easy","If __str__ is not defined, what is used?","__repr__","__format__","__init__","None","a","If __str__ is missing, Python falls back to __repr__.","oop"),
(python_id, oop_id, "medium","What is method resolution order (MRO)?","Order of execution","Order Python searches methods in inheritance","Method priority","Class hierarchy","b","MRO defines the order in which base classes are searched when executing a method.","oop"),
(python_id, oop_id, "medium","Which function shows MRO?","mro()","order()","dir()","method()","a","ClassName.mro() shows method resolution order.","oop"),
(python_id, oop_id, "medium","What is multiple inheritance issue called?","Diamond problem","Inheritance loop","Recursive class","Multi error","a","Diamond problem occurs when two parents inherit from same base class.","oop"),
(python_id, oop_id, "easy","What does super() do?","Calls parent class methods","Creates object","Deletes class","Overrides method","a","super() is used to access methods of the parent class.","oop"),
(python_id, oop_id, "medium","Can Python have private variables?","No","Yes with _var","Yes with __var (name mangling)","Only public","c","__var triggers name mangling to simulate private variables.","oop"),
(python_id, oop_id, "easy","If a class has no __init__, what happens?","Error","Default constructor used","Object not created","None","b","Python provides default constructor.","oop"),
(python_id, oop_id, "medium","Can we have multiple __init__ methods?","Yes","No","Only 2","Depends","b","Python does not support method overloading directly.","oop"),
(python_id, oop_id, "medium","How to simulate method overloading?","Inheritance","Default args / *args","Loop","Decorator","b","Use default args or variable arguments.","oop"),
(python_id, oop_id, "medium","What is method overloading in Python?","Not supported directly","Supported fully","Only in classes","Only in functions","a","Python uses dynamic typing instead.","oop"),
(python_id, oop_id, "easy","What is class variable?","Inside function","Shared across all instances","Local variable","Private variable","b","Class variables are shared among all objects.","oop"),


# ── PYTHON FUNCTIONS ──

(python_id, functions_id, "easy","When are default arguments evaluated?","At runtime","At function call","At function definition","Never","c","Default arguments are evaluated only once at function definition.","python,functions,defaults"),
(python_id, functions_id, "medium","What is the issue with mutable default arguments?","Syntax error","Shared state across calls","Performance issue","No issue","b","Mutable defaults retain changes across function calls.","python,functions,edge-case"),
(python_id, functions_id, "medium","What does 'nonlocal' do?","Access global variable","Modify enclosing scope variable","Create local variable","Delete variable","b","nonlocal allows modifying variables from enclosing scope.","python,functions,scope"),
(python_id, functions_id, "easy","What is first-class function?","Function inside class","Function as variable","Function without return","Built-in function","b","Functions can be assigned, passed, and returned.","python,functions,concept"),
(python_id, functions_id, "medium","What does closure mean?","Nested function","Function with preserved outer variables","Loop function","Recursive function","b","Closures remember values from enclosing scope even after it exits.","python,functions,closure"),
(python_id, functions_id, "easy","Which keyword defines a function?","func","def","function","define","b","'def' keyword is used to define a function in Python.","python,functions,basics"),
(python_id, functions_id, "easy","What is a lambda function?","A class method","An anonymous function","A recursive function","A built-in function","b","Lambda is an anonymous function defined with the lambda keyword.","python,functions,lambda"),
(python_id, functions_id, "easy","What does 'return' do?","Prints a value","Exits and sends back a value","Starts a loop","Creates a variable","b","'return' exits a function and sends a value back to the caller.","python,functions,basics"),
(python_id, functions_id, "easy","What is recursion?","A loop","A function calling itself","Multiple inheritance","Data hiding","b","Recursion is when a function calls itself.","python,functions,recursion"),
(python_id, functions_id, "easy","What are *args used for?","Keyword arguments","Variable number of positional arguments","Default arguments","Global variables","b","*args allows a function to accept any number of positional arguments.","python,functions,args"),
(python_id, functions_id, "easy","What are **kwargs used for?","Positional arguments","Variable number of keyword arguments","Default values","Class methods","b","**kwargs allows a function to accept keyword arguments.","python,functions,kwargs"),
(python_id, functions_id, "easy","What is a default argument?","Required argument","Argument with a preset value","Keyword argument","Variable argument","b","Default arguments have preset values.","python,functions,defaults"),
(python_id, functions_id, "easy","What is the scope of a local variable?","Entire program","Only inside the function","Only in classes","Only in loops","b","Local variables exist only inside the function.","python,functions,scope"),
(python_id, functions_id, "medium","What does map() do?","Filters elements","Applies function to each element","Sorts a list","Counts elements","b","map() applies a function to every element of an iterable.","python,functions,map"),
(python_id, functions_id, "medium","What does filter() do?","Applies function to all","Returns elements that pass a condition","Sorts elements","Counts elements","b","filter() returns elements where condition is True.","python,functions,filter"),
(python_id, functions_id, "hard","What is output? def f(x=[]): x.append(1); return x; print(f()); print(f())","[1],[1]","[1],[2]","[1],[1,1]","Error","c","Mutable default persists across calls.","python,functions,edge-case"),
(python_id, functions_id, "medium","What is output? def f(x=None): x=[] if x is None else x; x.append(1); return x","Error","Always new list","Shared list","None","b","Using None avoids mutable default issue.","python,functions,edge-case"),
(python_id, functions_id, "easy","What happens if function has no return?","Error","Returns None","Returns 0","Returns empty list","b","Python functions return None by default.","python,functions,basics"),
(python_id, functions_id, "easy","What is output? print((lambda x: x+1)(5))","5","6","Error","None","b","Lambda adds 1 → output 6.","python,functions,lambda"),
(python_id, functions_id, "medium","What is output? def f(a,b=2,c=3): return a+b+c; print(f(1,c=5))","6","8","Error","None","b","1 + 2 + 5 = 8.","python,functions,defaults"),


# ── PYTHON DECORATORS ──

(python_id, decorators_id, "easy","What is a decorator in Python?","Class","Function modifying another function","Loop","Variable","b","Decorators wrap a function to extend its behavior.","python,decorators,basics"),
(python_id, decorators_id, "easy","What symbol is used for decorators?","#","@","$","&","b","@ is used to apply decorators.","python,decorators,syntax"),
(python_id, decorators_id, "medium","What is required inside decorator?","Loop","Wrapper function","Class","Global variable","b","Decorator must define a wrapper function.","python,decorators,concept"),
(python_id, decorators_id, "medium","Can a decorator take arguments?","No","Yes","Only in classes","Only built-in","b","Decorators can take arguments using nested functions.","python,decorators,advanced"),
(python_id, decorators_id, "medium","What does functools.wraps do?","Copies metadata","Optimizes function","Runs function","Returns value","a","wraps preserves original function metadata like name and docstring.","python,decorators,functools"),
(python_id, decorators_id, "hard","What is output of decorator order?","Top runs first","Bottom runs first","Random","Error","b","Decorators execute bottom-up.","python,decorators,execution"),
(python_id, decorators_id, "medium","Can decorators modify arguments?","No","Yes","Only return","Only print","b","Decorators can intercept and modify arguments.","python,decorators,advanced"),
(python_id, decorators_id, "easy","What is chained decorator?","Multiple decorators","Recursive decorator","Loop decorator","Class decorator","a","Stacking multiple decorators.","python,decorators,concept"),


# ── PYTHON GENERATORS ──

(python_id, generators_id, "medium","What is send() in generator?","Stop generator","Send value into generator","Restart generator","Delete generator","b","send() resumes generator and can pass a value inside it.","python,generators,advanced"),
(python_id, generators_id, "easy","Difference: generator vs iterator?","Same","Generator is simpler way to create iterator","Iterator faster","No diff","b","Generators are a simpler way to create iterators using yield.","python,generators,concept"),
(python_id, generators_id, "medium","What is yield from?","Stop yield","Delegate to another generator","Return value","Error","b","'yield from' delegates iteration to another generator.","python,generators,advanced"),


# ── NUMPY ──

(python_id, numpy_id, 'easy', "What is NumPy mainly used for?", "Web development","Numerical computing","Database management","Networking","b","NumPy is used for efficient numerical computations with arrays.","python,numpy,basics"),
(python_id, numpy_id, 'easy', "What is ndarray?", "List","NumPy array object","Dictionary","Tuple","b","ndarray is the core data structure in NumPy.","python,numpy,basics"),
(python_id, numpy_id, 'easy', "Which is faster? Python list or NumPy array?", "List","Array","Same","Depends","b","NumPy arrays are faster due to vectorization.","python,numpy,performance"),
(python_id, numpy_id, 'easy', "What does shape return?", "Size","Dimensions of array","Data type","Index","b","shape returns tuple representing array dimensions.","python,numpy,basics"),
(python_id, numpy_id, 'easy', "What does dtype represent?", "Shape","Index","Data type","Size","c","dtype specifies type of elements in array.","python,numpy,basics"),
(python_id, numpy_id, 'medium', "What is broadcasting?", "Copying arrays","Expanding arrays automatically","Sorting","Filtering","b","Broadcasting allows operations on arrays of different shapes.","python,numpy,advanced"),
(python_id, numpy_id, 'easy', "What will np.zeros((2,2)) create?", "List","2x2 array of zeros","Error","Tuple","b","Creates a 2x2 matrix filled with zeros.","python,numpy,basics"),
(python_id, numpy_id, 'medium', "What is vectorization?", "Looping","Applying operations without loops","Sorting arrays","Filtering","b","Vectorization avoids explicit loops and improves performance.","python,numpy,performance"),
(python_id, numpy_id, 'medium', "What is axis=0 in sum()?", "Row-wise","Column-wise","Flatten","Error","b","axis=0 means operate column-wise.","python,numpy,operations"),
(python_id, numpy_id, 'medium', "What is axis=1?", "Row-wise","Column-wise","Error","Flatten","a","axis=1 means operate row-wise.","python,numpy,operations"),
(python_id, numpy_id, 'easy', "What is output? np.array([1,2,3]) + 1", "[1,2,3]","[2,3,4]","Error","None","b","Broadcasting adds 1 to each element.","python,numpy,operations"),
(python_id, numpy_id, 'easy', "What is shape of np.array([[1,2],[3,4]])?", "(2,)","(2,2)","(4,)","Error","b","2 rows, 2 columns.","python,numpy,basics"),
(python_id, numpy_id, 'medium', "Which is faster for large ops?", "Loop","Vectorized NumPy","Same","Depends","b","Vectorized operations are optimized in C.","python,numpy,performance"),


# ── PANDAS ──

(python_id, pandas_id, 'easy', "What is Pandas used for?", "Game dev","Data manipulation","Networking","UI design","b","Pandas is used for data analysis and manipulation.","python,pandas,basics"),
(python_id, pandas_id, 'easy', "What are main Pandas structures?", "Array, List","Series, DataFrame","Tuple, Dict","Stack, Queue","b","Series and DataFrame are core structures.","python,pandas,basics"),
(python_id, pandas_id, 'easy', "What is a DataFrame?", "1D array","2D tabular data","Graph","Tree","b","DataFrame is a 2D labeled data structure.","python,pandas,basics"),
(python_id, pandas_id, 'easy', "What does head() do?", "Last rows","First rows","Middle rows","Random rows","b","head() returns first n rows.","python,pandas,basics"),
(python_id, pandas_id, 'easy', "What does tail() do?", "First rows","Last rows","Middle rows","Random rows","b","tail() returns last n rows.","python,pandas,basics"),
(python_id, pandas_id, 'easy', "What does isnull() do?", "Delete nulls","Check missing values","Fill values","Sort data","b","isnull() identifies missing values.","python,pandas,cleaning"),
(python_id, pandas_id, 'easy', "How to fill missing values?", "dropna()","fillna()","remove()","replace()","b","fillna() fills missing values.","python,pandas,cleaning"),
(python_id, pandas_id, 'medium', "What does groupby() do?", "Sort data","Group data for aggregation","Join tables","Filter rows","b","groupby() groups data for aggregation.","python,pandas,aggregation"),
(python_id, pandas_id, 'medium', "What is merge() used for?", "Sorting","Joining DataFrames","Filtering","Grouping","b","merge() joins DataFrames like SQL joins.","python,pandas,joins"),
(python_id, pandas_id, 'medium', "What does apply() do?", "Delete column","Apply function to rows/columns","Sort data","Filter rows","b","apply() applies custom function.","python,pandas,functions"),
(python_id, pandas_id, 'easy', "What is loc[]?", "Index by position","Index by label","Filter only","Sort only","b","loc[] is label-based indexing.","python,pandas,indexing"),
(python_id, pandas_id, 'easy', "What is iloc[]?", "Label index","Position index","Filter","Sort","b","iloc[] is integer position-based indexing.","python,pandas,indexing"),
(python_id, pandas_id, 'easy', "What does describe() return?", "Raw data","Summary stats","Sorted data","Null values","b","describe() returns statistical summary.","python,pandas,eda"),
(python_id, pandas_id, 'easy', "What does value_counts() do?", "Counts unique values","Sort values","Group data","Merge data","a","value_counts() counts frequency of unique values.","python,pandas,eda"),
(python_id, pandas_id, 'medium', "What is pivot table?", "Sorting","Reshaping data","Deleting data","Filtering","b","Pivot reshapes and aggregates data.","python,pandas,aggregation"),
(python_id, pandas_id, 'easy', "What happens if you dropna()?", "Fill values","Remove rows with nulls","Sort data","Error","b","dropna removes rows with missing values.","python,pandas,cleaning"),
(python_id, pandas_id, 'easy', "What does df['col'].unique() do?", "Counts values","Returns unique values","Sorts values","Deletes duplicates","b","unique() returns distinct values.","python,pandas,eda"),
(python_id, pandas_id, 'medium', "What is output type of groupby()?", "List","DataFrameGroupBy object","Dictionary","Series","b","groupby returns groupby object.","python,pandas,aggregation"),
(python_id, pandas_id, 'medium', "When to use apply vs map?", "Same","apply for DataFrame, map for Series","map faster always","apply only numeric","b","map is for Series, apply works on both axes.","python,pandas,functions"),
(python_id, pandas_id, 'easy', "What does inplace=True do?", "Copy data","Modify original","Delete data","Error","b","It modifies the original DataFrame.","python,pandas,basics"),
(python_id, pandas_id, 'medium', "You have missing ages. Best approach?", "Drop all rows","Fill with 0","Fill with mean/median","Ignore missing","c","Mean/median preserves data.","python,pandas,cleaning"),
(python_id, pandas_id, 'medium', "Sales data has extreme outliers. What to do?", "Delete all data","Ignore","Cap or remove outliers","Duplicate data","c","Outliers distort analysis.","python,pandas,eda"),
(python_id, pandas_id, 'easy', "Dataset has duplicate rows. Best approach?", "Ignore","Drop duplicates","Sort data","Group data","b","drop_duplicates() removes redundancy.","python,pandas,cleaning"),
(python_id, pandas_id, 'medium', "Average sales per region?", "sort_values()","groupby()","merge()","apply()","b","groupby('region').mean().","python,pandas,aggregation"),
(python_id, pandas_id, 'easy', "Inconsistent column names. First step?", "Train model","Rename columns","Delete columns","Sort data","b","Standardize column names first.","python,pandas,cleaning"),
(python_id, pandas_id, 'easy', "Join customer and order data?", "groupby","merge","apply","concat","b","merge is used for joins.","python,pandas,joins"),
(python_id, pandas_id, 'medium', "When use left join?", "Only matching","Keep all left","Keep all right","Drop nulls","b","Left join keeps all left records.","python,pandas,joins"),
(python_id, pandas_id, 'medium', "Top 5 selling products?", "groupby + sort","merge","apply","dropna","a","group + sort + head(5).","python,pandas,analysis"),
(python_id, pandas_id, 'easy', "String dates column?", "Ignore","Convert to datetime","Delete","Sort","b","pd.to_datetime() converts to datetime.","python,pandas,dates"),
(python_id, pandas_id, 'medium', "Monthly sales trend?", "Group by month","Sort","Drop nulls","Merge","a","Extract month and group.","python,pandas,time-series"),
(python_id, pandas_id, 'medium', "Categorical variable handling?", "Ignore","One-hot encoding","Drop","Sort","b","Use encoding.","python,pandas,ml-prep"),
(python_id, pandas_id, 'medium', "Large dataset memory issue?", "Use list","Use Pandas","Use chunk processing","Duplicate","c","Chunk processing solves memory issues.","python,pandas,performance"),
(python_id, pandas_id, 'easy', "Correlation method?", "describe()","corr()","groupby()","merge()","b","corr() computes correlation.","python,pandas,eda"),
(python_id, pandas_id, 'easy', "Filter sales > 1000?", "groupby","Boolean filtering","merge","apply","b","Use condition filtering.","python,pandas,filter"),
(python_id, pandas_id, 'medium', "Skewed data handling?", "Ignore","Log transform","Delete","Sort","b","Log reduces skewness.","python,pandas,eda"),
(python_id, pandas_id, 'medium', "Rolling average?", "mean()","rolling()","groupby()","apply()","b","rolling() computes moving average.","python,pandas,time-series"),
(python_id, pandas_id, 'easy', "Cumulative sum?", "sum()","cumsum()","mean()","rolling()","b","cumsum() gives cumulative total.","python,pandas,operations"),
(python_id, pandas_id, 'medium', "Missing categorical values?", "Fill with mode","Fill with mean","Delete","Ignore","a","Mode is best for categorical.","python,pandas,cleaning"),
(python_id, pandas_id, 'medium', "Detect duplicates column-wise?", "dropna()","duplicated()","merge()","apply()","b","duplicated() finds duplicates.","python,pandas,cleaning"),
(python_id, pandas_id, 'medium', "Sort by multiple columns?", "sort_values()","groupby()","apply()","merge()","a","sort_values(by=[...]).","python,pandas,sorting"),
(python_id, pandas_id, 'hard', "E-commerce sales drop?", "Train model","Check data quality","Deploy","Ignore","b","Always validate data first.","python,pandas,analysis"),
(python_id, pandas_id, 'medium', "User engagement drop?", "Model accuracy","A/B test results","Sort","Drop","b","A/B testing validates impact.","python,pandas,analysis"),
(python_id, pandas_id, 'medium', "High null important column?", "Ignore","Impute carefully","Delete dataset","Sort","b","Imputation depends on context.","python,pandas,cleaning"),
(python_id, pandas_id, 'medium', "Revenue up but profit down?", "Bug","Cost increased","Data issue","Random","b","Costs may increase.","python,pandas,business"),
(python_id, pandas_id, 'medium', "Imbalanced dataset?", "Ignore","Resampling","Delete minority","Sort","b","Use resampling techniques.","python,pandas,ml"),
(python_id, pandas_id, 'medium', "Detect anomaly?", "Sorting","Statistical threshold","Merge","Apply","b","Use z-score/IQR.","python,pandas,eda"),
(python_id, pandas_id, 'easy', "KPI dashboard first step?", "Plot graph","Define metrics","Train model","Clean data","b","Define metrics first.","python,pandas,business"),
(python_id, pandas_id, 'medium', "Inconsistent data sources?", "Merge directly","Standardize data","Ignore","Delete","b","Standardization is required.","python,pandas,cleaning"),
(python_id, pandas_id, 'medium', "Customer churn first step?", "Train model","Define churn","Plot","Group","b","Define churn clearly.","python,pandas,business"),
(python_id, pandas_id, 'medium', "Compare two campaigns?", "Sorting","A/B testing","Merge","Groupby","b","A/B testing compares performance.","python,pandas,analysis"),

# ── PYTHON DSA PATTERNS ──

(python_id, dsa_patterns_id, "easy", "What is sliding window used for?", "Sorting", "Subarray problems", "Graphs", "Trees", "b", "Sliding window is used for subarray/substring optimization.", "dsa,sliding_window"),
(python_id, dsa_patterns_id, "easy", "What is time complexity of sliding window?", "O(n²)", "O(n)", "O(log n)", "O(1)", "b", "Sliding window reduces nested loops to linear time.", "dsa,complexity"),
(python_id, dsa_patterns_id, "easy", "Two pointer technique is used in?", "Trees", "Arrays/strings", "Graphs", "Hashing only", "b", "Two pointers are used for sorted arrays and string problems.", "dsa,two_pointers"),
(python_id, dsa_patterns_id, "easy", "What is hashing used for?", "Sorting", "Fast lookup", "Recursion", "Graph traversal", "b", "Hashing provides O(1) average lookup.", "dsa,hashing"),
(python_id, dsa_patterns_id, "easy", "Time complexity of dictionary lookup?", "O(n)", "O(log n)", "O(1)", "O(n²)", "c", "Dictionary lookup is average O(1).", "dsa,hashing"),
(python_id, dsa_patterns_id, "easy", "What is prefix sum used for?", "Sorting", "Range sum queries", "Graph traversal", "Recursion", "b", "Prefix sum helps compute range sums efficiently.", "dsa,prefix_sum"),
(python_id, dsa_patterns_id, "easy", "What is brute force approach?", "Optimized", "Try all possibilities", "Hashing", "Recursion", "b", "Brute force checks all possibilities.", "dsa,basics"),
(python_id, dsa_patterns_id, "easy", "What is optimization goal in DSA?", "Increase loops", "Reduce time/space complexity", "Add memory", "Use recursion always", "b", "Goal is to optimize time and space.", "dsa,basics"),
(python_id, dsa_patterns_id, "easy", "What is recursion base case?", "Loop", "Stopping condition", "Input", "Output", "b", "Base case stops recursion.", "dsa,recursion"),
(python_id, dsa_patterns_id, "easy", "Stack is used in which pattern?", "Sorting", "DFS/recursion", "Hashing", "Arrays", "b", "Stack helps in recursion and DFS.", "dsa,stack"),
(python_id, dsa_patterns_id, "easy", "Queue is used in?", "DFS", "BFS", "Sorting", "Recursion", "b", "Queue is used in BFS traversal.", "dsa,queue"),
(python_id, dsa_patterns_id, "easy", "What is time complexity of BFS?", "O(n²)", "O(n + e)", "O(log n)", "O(1)", "b", "BFS traverses all nodes and edges.", "dsa,bfs"),
(python_id, dsa_patterns_id, "easy", "What is greedy approach?", "Try all", "Choose best at each step", "Recursion", "Backtracking", "b", "Greedy makes optimal choice at each step.", "dsa,greedy"),
(python_id, dsa_patterns_id, "easy", "What is backtracking?", "Greedy", "Try and undo", "Hashing", "Sorting", "b", "Backtracking explores all possibilities with pruning.", "dsa,backtracking"),
(python_id, dsa_patterns_id, "easy", "When to use set in problems?", "Sorting", "Remove duplicates", "Traversal", "Recursion", "b", "Set helps remove duplicates and fast lookup.", "dsa,set"),
(python_id, dsa_patterns_id, "easy", "Find duplicates fastest?", "Nested loop", "Sorting", "Set", "Recursion", "c", "Set gives O(n) solution.", "dsa,set"),
(python_id, dsa_patterns_id, "easy", "Longest substring without repeating chars uses?", "Sorting", "Sliding window", "Recursion", "Graph", "b", "Classic sliding window problem.", "dsa,sliding_window"),
(python_id, dsa_patterns_id, "easy", "Two sum optimal approach?", "Brute force", "Sorting", "Hash map", "Recursion", "c", "Hash map gives O(n) solution.", "dsa,hashing"),
(python_id, dsa_patterns_id, "easy", "Check palindrome efficiently?", "Reverse string", "Two pointers", "Loop", "Hashing", "b", "Two pointers from both ends.", "dsa,two_pointers"),
(python_id, dsa_patterns_id, "easy", "Detect cycle in linked list?", "Sorting", "Hashing", "Floyd’s cycle detection", "Recursion", "c", "Fast & slow pointer approach.", "dsa,linked_list"),
(python_id, dsa_patterns_id, "easy", "When to use heap?", "Sorting", "Top-K problems", "Recursion", "Hashing", "b", "Heap is best for priority/top-k problems.", "dsa,heap"),
(python_id, dsa_patterns_id, "easy", "DFS uses which DS?", "Queue", "Stack", "Array", "Hash", "b", "DFS uses stack (explicit or recursion).", "dsa,dfs"),
(python_id, dsa_patterns_id, "easy", "BFS shortest path in unweighted graph?", "No", "Yes", "Only weighted", "Depends", "b", "BFS guarantees shortest path in unweighted graph.", "dsa,bfs"),


# ── SQL JOINS ──


(sql_id, sql_joins_id, "easy", "What is an INNER JOIN?", "Returns all rows", "Returns matching rows from both tables", "Returns left table", "Returns right table", "b", "INNER JOIN returns only matching rows from both tables.", "sql,joins,inner"),
(sql_id, sql_joins_id, "easy", "What does LEFT JOIN return?", "Only matching rows", "All left + matching right", "Only right", "None", "b", "LEFT JOIN returns all rows from left table and matching rows from right.", "sql,joins,left"),
(sql_id, sql_joins_id, "easy", "What does RIGHT JOIN return?", "All left", "All right + matching left", "Only matching", "None", "b", "RIGHT JOIN returns all rows from right table and matching from left.", "sql,joins,right"),
(sql_id, sql_joins_id, "medium", "What does FULL OUTER JOIN return?", "Only left", "Only right", "All rows from both tables", "Only matching", "c", "Returns all rows, matched or unmatched.", "sql,joins,full"),
(sql_id, sql_joins_id, "easy", "What is CROSS JOIN?", "Matching rows", "Cartesian product", "Filtered rows", "Grouped rows", "b", "CROSS JOIN returns all combinations.", "sql,joins,cross"),
(sql_id, sql_joins_id, "medium", "Which join returns unmatched rows only?", "INNER", "LEFT", "ANTI JOIN", "RIGHT", "c", "ANTI JOIN returns non-matching rows.", "sql,joins,advanced"),
(sql_id, sql_joins_id, "easy", "Which clause is used for join condition?", "WHERE", "ON", "GROUP BY", "ORDER BY", "b", "ON defines join condition.", "sql,joins,syntax"),
(sql_id, sql_joins_id, "medium", "Difference: WHERE vs ON?", "Same", "ON filters before join", "WHERE filters after join", "Both b & c", "d", "ON applies during join, WHERE after.", "sql,joins,concept"),
(sql_id, sql_joins_id, "medium", "Self join is used for?", "Same table", "Different tables", "Aggregation", "Sorting", "a", "Self join joins table to itself.", "sql,joins,self"),
(sql_id, sql_joins_id, "easy", "Join without condition gives?", "Error", "Cartesian product", "Filtered rows", "Sorted rows", "b", "No condition → CROSS JOIN behavior.", "sql,joins,concept"),
(sql_id, sql_joins_id, "medium", "What is equi join?", "Uses =", "Uses >", "Uses <", "Uses LIKE", "a", "Equi join uses equality condition.", "sql,joins,equi"),
(sql_id, sql_joins_id, "medium", "Non-equi join uses?", "= only", "Other operators", "No condition", "Group by", "b", "Uses >, <, BETWEEN etc.", "sql,joins,non-equi"),
(sql_id, sql_joins_id, "easy", "Which join keeps all records from left?", "INNER", "LEFT", "RIGHT", "FULL", "b", "LEFT JOIN keeps all left records.", "sql,joins,left"),
(sql_id, sql_joins_id, "easy", "Which join keeps all records from right?", "INNER", "LEFT", "RIGHT", "FULL", "c", "RIGHT JOIN keeps all right records.", "sql,joins,right"),
(sql_id, sql_joins_id, "medium", "How to find unmatched left rows?", "INNER JOIN", "LEFT JOIN + IS NULL", "RIGHT JOIN", "GROUP BY", "b", "Use LEFT JOIN and filter NULL.", "sql,joins,practice"),
(sql_id, sql_joins_id, "medium", "Join on multiple columns?", "Not possible", "Use AND", "Use OR", "Use GROUP BY", "b", "Multiple conditions with AND.", "sql,joins,syntax"),
(sql_id, sql_joins_id, "easy", "Which join gives common data?", "INNER", "LEFT", "RIGHT", "FULL", "a", "INNER JOIN gives common rows.", "sql,joins,inner"),
(sql_id, sql_joins_id, "medium", "Join performance depends on?", "Indexes", "Table size", "Query design", "All", "d", "All factors affect performance.", "sql,joins,performance"),
(sql_id, sql_joins_id, "medium", "What is natural join?", "Auto join by column names", "Manual join", "Cross join", "None", "a", "Joins using same column names.", "sql,joins,natural"),
(sql_id, sql_joins_id, "hard", "Duplicate rows in join reason?", "Wrong condition", "Missing join key", "Data duplication", "All", "d", "Improper joins create duplicates.", "sql,joins,debug"),
(sql_id, sql_joins_id, "easy", "What is an INNER JOIN?","Returns all rows","Returns matching rows from both tables","Returns left table only","Returns right table only","b","INNER JOIN returns only matching rows from both tables.","sql,joins"),
(sql_id, sql_joins_id, "easy", "What is a LEFT JOIN?","Only matching rows","All left + matched right","All right + matched left","Only right","b","LEFT JOIN returns all rows from left table and matched rows from right.","sql,joins"),
(sql_id, sql_joins_id, "easy", "What is a RIGHT JOIN?","All left","All right + matched left","Only matching","Cross product","b","RIGHT JOIN returns all rows from right table and matched rows from left.","sql,joins"),
(sql_id, sql_joins_id, "easy", "What is FULL OUTER JOIN?","Only left","Only right","Only matching","All rows from both tables","d","FULL JOIN returns all rows with NULLs where no match.","sql,joins"),
(sql_id, sql_joins_id, "easy", "What happens when no match in LEFT JOIN?","Row removed","Error","NULLs in right table","Duplicate row","c","Unmatched rows get NULL values for right table.","sql,joins"),
(sql_id, sql_joins_id, "medium", "What is CROSS JOIN?","Matching rows","Cartesian product","Left join","Right join","b","CROSS JOIN returns all combinations of rows.","sql,joins"),
(sql_id, sql_joins_id, "medium", "What is SELF JOIN?","Join same table","Join 2 tables","Recursive join","Outer join","a","SELF JOIN joins a table with itself.","sql,joins"),
(sql_id, sql_joins_id, "medium", "Which join keeps unmatched rows from both tables?","INNER","LEFT","RIGHT","FULL","d","FULL JOIN keeps all rows from both tables.","sql,joins"),
(sql_id, sql_joins_id, "medium", "Join condition is written using?","WHERE only","ON clause","GROUP BY","HAVING","b","ON defines join condition.","sql,joins"),
(sql_id, sql_joins_id, "medium", "Difference: ON vs WHERE in joins?","Same","ON filters before join","WHERE filters after join","No diff","c","ON applies join condition, WHERE filters result.","sql,joins"),
(sql_id, sql_joins_id, "hard", "Find unmatched rows in left table?","INNER JOIN","LEFT JOIN + WHERE NULL","RIGHT JOIN","CROSS JOIN","b","Use LEFT JOIN and filter NULLs.","sql,joins"),
(sql_id, sql_joins_id, "hard", "Which join is fastest generally?","INNER","LEFT","RIGHT","FULL","a","INNER JOIN is usually fastest due to fewer rows.","sql,joins"),
(sql_id, sql_joins_id, "hard", "Duplicate rows in join occur when?","No match","Many-to-many relation","NULL values","Sorting","b","Duplicates occur in many-to-many joins.","sql,joins"),
(sql_id, sql_joins_id, "hard", "What is equi join?","Using = condition","Using >","Using <","No condition","a","Equi join uses equality condition.","sql,joins"),
(sql_id, sql_joins_id, "hard", "What is non-equi join?","Using =","Using conditions like >, <","No join","Inner join","b","Non-equi joins use inequality conditions.","sql,joins"),
(sql_id, sql_joins_id, "medium", "Join 3 tables requires?","One join","Two joins","Three joins","Not possible","b","To join 3 tables, you need 2 joins.","sql,joins"),
(sql_id, sql_joins_id, "medium", "What is alias in join?","Rename table","Delete table","Sort table","Group table","a","Aliases shorten table names in queries.","sql,joins"),
(sql_id, sql_joins_id, "medium", "What happens if join condition missing?","Error","Cartesian product","No rows","NULL rows","b","Missing condition leads to CROSS JOIN.","sql,joins"),
(sql_id, sql_joins_id, "medium", "Which join returns only non-matching rows?","INNER","LEFT + NULL filter","RIGHT","FULL","b","LEFT JOIN + WHERE NULL gives non-matching rows.","sql,joins"),
(sql_id, sql_joins_id, "hard", "Best join for large tables?","FULL","CROSS","INNER with index","SELF","c","Indexes + INNER JOIN improve performance.","sql,joins"),

# ── SQL BASIC QUERIES ──

(sql_id, sql_basic_id, "easy", "Which keyword selects data?", "GET", "SELECT", "FETCH", "SHOW", "b", "SELECT is used to retrieve data.", "sql,basics"),
(sql_id, sql_basic_id, "easy", "Which clause filters rows?", "GROUP BY", "WHERE", "ORDER BY", "JOIN", "b", "WHERE filters rows.", "sql,basics"),
(sql_id, sql_basic_id, "easy", "Which clause sorts data?", "WHERE", "ORDER BY", "GROUP BY", "JOIN", "b", "ORDER BY sorts results.", "sql,basics"),
(sql_id, sql_basic_id, "easy", "Default sort order?", "DESC", "ASC", "RANDOM", "NONE", "b", "ASC is default.", "sql,basics"),
(sql_id, sql_basic_id, "easy", "COUNT(*) does?", "Counts rows", "Counts columns", "Counts nulls", "Counts values", "a", "Counts all rows.", "sql,aggregation"),
(sql_id, sql_basic_id, "easy", "Which clause groups data?", "WHERE", "GROUP BY", "ORDER BY", "JOIN", "b", "GROUP BY groups rows.", "sql,aggregation"),
(sql_id, sql_basic_id, "easy", "HAVING is used with?", "WHERE", "GROUP BY", "ORDER BY", "JOIN", "b", "HAVING filters grouped data.", "sql,aggregation"),
(sql_id, sql_basic_id, "medium", "Difference WHERE vs HAVING?", "Same", "WHERE before grouping", "HAVING after grouping", "Both b & c", "d", "WHERE before, HAVING after.", "sql,concept"),
(sql_id, sql_basic_id, "easy", "Which function finds max?", "MAX()", "TOP()", "HIGH()", "UP()", "a", "MAX returns highest value.", "sql,functions"),
(sql_id, sql_basic_id, "easy", "Which function finds average?", "AVG()", "MEAN()", "MID()", "CENTER()", "a", "AVG calculates average.", "sql,functions"),
(sql_id, sql_basic_id, "easy", "LIKE is used for?", "Sorting", "Pattern matching", "Grouping", "Joining", "b", "LIKE matches patterns.", "sql,basics"),
(sql_id, sql_basic_id, "easy", "Wildcard for multiple chars?", "_", "%", "*", "#", "b", "% matches multiple chars.", "sql,like"),
(sql_id, sql_basic_id, "easy", "Wildcard for single char?", "_", "%", "*", "#", "a", "_ matches one char.", "sql,like"),
(sql_id, sql_basic_id, "medium", "NULL means?", "Zero", "Empty", "Unknown", "False", "c", "NULL represents missing value.", "sql,null"),
(sql_id, sql_basic_id, "easy", "Check NULL?", "= NULL", "IS NULL", "== NULL", "NULL()", "b", "Use IS NULL.", "sql,null"),
(sql_id, sql_basic_id, "easy", "Remove duplicates?", "DISTINCT", "UNIQUE", "FILTER", "GROUP", "a", "DISTINCT removes duplicates.", "sql,basics"),
(sql_id, sql_basic_id, "medium", "LIMIT is used for?", "Filtering", "Sorting", "Restrict rows", "Grouping", "c", "LIMIT restricts output rows.", "sql,basics"),
(sql_id, sql_basic_id, "easy", "Alias keyword?", "AS", "ALIAS", "NAME", "TAG", "a", "AS renames column.", "sql,basics"),
(sql_id, sql_basic_id, "medium", "Subquery is?", "Nested query", "Join", "Group", "Sort", "a", "Query inside query.", "sql,subquery"),
(sql_id, sql_basic_id, "hard", "Order of execution?", "SELECT→WHERE", "WHERE→SELECT", "FROM→WHERE→SELECT", "SELECT→FROM→WHERE", "c", "Execution starts from FROM.", "sql,execution"),


# ── SQL WINDOW FUNCTIONS ──

(sql_id, sql_window_id, "easy", "What is a window function?","Aggregate only","Operates on row sets without grouping","Only joins","Deletes rows","b","Window functions perform calculations across a set of rows without collapsing them.","sql,window"),
(sql_id, sql_window_id, "easy", "Which clause is used with window functions?","GROUP BY","OVER()","WHERE","JOIN","b","Window functions use OVER() clause.","sql,window"),
(sql_id, sql_window_id, "easy", "What does ROW_NUMBER() do?","Counts rows","Assigns unique row numbers","Finds duplicates","Groups rows","b","ROW_NUMBER assigns unique sequential numbers.","sql,window"),
(sql_id, sql_window_id, "easy", "What does RANK() do?","Unique ranking","Ranking with gaps","No ranking","Sort only","b","RANK assigns rank with gaps for ties.","sql,window"),
(sql_id, sql_window_id, "easy", "What does DENSE_RANK() do?","Ranking with gaps","Ranking without gaps","Counts rows","Sorts data","b","DENSE_RANK assigns rank without gaps.","sql,window"),
(sql_id, sql_window_id, "medium", "Difference ROW_NUMBER vs RANK?","Same","ROW_NUMBER unique, RANK allows ties","RANK faster","No diff","b","ROW_NUMBER gives unique numbers, RANK handles ties.","sql,window"),
(sql_id, sql_window_id, "medium", "What is PARTITION BY?","Filters rows","Groups rows for window function","Sorts rows","Deletes rows","b","PARTITION BY divides rows into groups.","sql,window"),
(sql_id, sql_window_id, "medium", "What is ORDER BY in window function?","Filter","Defines order within partition","Join condition","Grouping","b","ORDER BY defines order inside window.","sql,window"),
(sql_id, sql_window_id, "medium", "What does SUM() OVER() do?","Aggregate all","Running total","Deletes rows","Counts rows","b","SUM OVER gives cumulative sum.","sql,window"),
(sql_id, sql_window_id, "medium", "What is running total?","Total sum","Cumulative sum over rows","Average","Count","b","Running total accumulates values row by row.","sql,window"),
(sql_id, sql_window_id, "hard", "What does LAG() do?","Next row","Previous row value","Sum values","Rank rows","b","LAG accesses previous row value.","sql,window"),
(sql_id, sql_window_id, "hard", "What does LEAD() do?","Previous row","Next row value","Sort rows","Join tables","b","LEAD accesses next row value.","sql,window"),
(sql_id, sql_window_id, "hard", "What is difference LAG vs LEAD?","Same","LAG previous, LEAD next","LEAD faster","No diff","b","They access previous and next rows respectively.","sql,window"),
(sql_id, sql_window_id, "hard", "What is window frame?","Table","Subset of partition","Index","Join","b","Frame defines subset of rows for calculation.","sql,window"),
(sql_id, sql_window_id, "hard", "Default window frame?","Entire table","Current row","Range between unbounded preceding and current row","None","c","Default frame depends on function but often cumulative.","sql,window"),
(sql_id, sql_window_id, "medium", "Find top 1 per group?","GROUP BY","ROW_NUMBER() with PARTITION","JOIN","HAVING","b","Use ROW_NUMBER partitioned by group.","sql,window"),
(sql_id, sql_window_id, "medium", "Remove duplicates keep latest?","DELETE","ROW_NUMBER filter","GROUP BY","JOIN","b","Use ROW_NUMBER and filter row_num=1.","sql,window"),
(sql_id, sql_window_id, "medium", "Nth highest salary?","GROUP BY","RANK/DENSE_RANK","JOIN","COUNT","b","Ranking functions solve Nth value problems.","sql,window"),
(sql_id, sql_window_id, "medium", "Difference GROUP BY vs window?","Same","GROUP BY collapses rows, window doesn't","Window faster","No diff","b","Window keeps rows intact.","sql,window"),
(sql_id, sql_window_id, "hard", "Which is more flexible?","GROUP BY","Window functions","JOIN","WHERE","b","Window functions allow complex analytics without grouping.","sql,window"),


# ── SQL CTE (Common Table Expressions) ──


(sql_id, sql_cte_id, "easy", "What is a CTE?","Temporary table","Permanent table","Subquery","Index","a","CTE is a temporary result set defined using WITH.","sql,cte"),
(sql_id, sql_cte_id, "easy", "Which keyword defines a CTE?","SELECT","WITH","CREATE","TEMP","b","CTE is defined using WITH keyword.","sql,cte"),
(sql_id, sql_cte_id, "easy", "CTE is stored where?","Disk","Memory (temporary)","Index","Table","b","CTEs exist temporarily during query execution.","sql,cte"),
(sql_id, sql_cte_id, "easy", "CTE improves?","Speed always","Readability","Indexing","Storage","b","CTEs improve readability and structure.","sql,cte"),
(sql_id, sql_cte_id, "easy", "Can CTE be reused?","No","Yes within query","Globally","Only once","b","CTE can be referenced multiple times in same query.","sql,cte"),
(sql_id, sql_cte_id, "medium", "Difference CTE vs subquery?","Same","CTE is reusable and readable","Subquery faster always","No diff","b","CTE improves readability and reuse.","sql,cte"),
(sql_id, sql_cte_id, "medium", "Can we use multiple CTEs?","No","Yes separated by comma","Only 2","Only 1","b","Multiple CTEs can be defined with commas.","sql,cte"),
(sql_id, sql_cte_id, "medium", "What is recursive CTE?","Loop query","CTE calling itself","Join query","Group query","b","Recursive CTE references itself.","sql,cte"),
(sql_id, sql_cte_id, "medium", "Recursive CTE needs?","Loop","Anchor + recursive part","Join","Index","b","It requires base (anchor) and recursive query.","sql,cte"),
(sql_id, sql_cte_id, "medium", "Which keyword combines recursive parts?","JOIN","UNION ALL","GROUP BY","WHERE","b","Recursive CTE uses UNION ALL.","sql,cte"),
(sql_id, sql_cte_id, "hard", "CTE vs temp table?","Same","CTE not stored physically","Temp table faster always","No diff","b","CTE is not stored physically unlike temp tables.","sql,cte"),
(sql_id, sql_cte_id, "hard", "Can CTE be indexed?","Yes","No","Only sometimes","Depends","b","CTEs cannot be indexed.","sql,cte"),
(sql_id, sql_cte_id, "hard", "When CTE is evaluated?","Compile time","Execution time","Runtime later","Never","b","CTEs are evaluated during query execution.","sql,cte"),
(sql_id, sql_cte_id, "hard", "CTE scope?","Global","Session","Single query","Database","c","CTE exists only within query scope.","sql,cte"),
(sql_id, sql_cte_id, "hard", "Recursive CTE risk?","Speed","Infinite loop","Join error","Syntax error","b","Wrong condition may cause infinite recursion.","sql,cte"),
(sql_id, sql_cte_id, "medium", "Use case of CTE?","Indexing","Breaking complex queries","Sorting","Deleting","b","CTE simplifies complex logic.","sql,cte"),
(sql_id, sql_cte_id, "medium", "CTE with window functions?","No","Yes","Only once","Not possible","b","CTEs often combined with window functions.","sql,cte"),
(sql_id, sql_cte_id, "medium", "Can CTE replace subquery?","No","Yes often","Never","Only joins","b","CTEs can replace nested subqueries.","sql,cte"),
(sql_id, sql_cte_id, "medium", "Recursive CTE used for?","Sorting","Hierarchical data","Joining","Filtering","b","Used for trees, org charts, etc.","sql,cte"),
(sql_id, sql_cte_id, "hard", "Performance of CTE?","Always faster","Depends on query","Always slow","Same","b","Performance depends on DB optimizer.","sql,cte"),


# ── SQL INDEXING (REAL PERFORMANCE SCENARIOS) ──


(sql_id, sql_indexing_id, "easy", "What is an index in SQL?","Data table","Data structure for fast lookup","Join method","Constraint","b","Index speeds up data retrieval.","sql,indexing"),
(sql_id, sql_indexing_id, "easy", "Index improves?","Insert speed","Read/query speed","Delete only","Nothing","b","Indexes optimize SELECT queries.","sql,indexing"),
(sql_id, sql_indexing_id, "easy", "Primary key creates?","No index","Index automatically","Join","View","b","Primary key creates clustered index by default.","sql,indexing"),
(sql_id, sql_indexing_id, "easy", "Unique index ensures?","Duplicates allowed","No duplicates","Sorting","Grouping","b","Unique index prevents duplicate values.","sql,indexing"),
(sql_id, sql_indexing_id, "easy", "Clustered index stores?","Pointers","Actual data order","Temp data","Join results","b","Clustered index defines physical order of data.","sql,indexing"),
(sql_id, sql_indexing_id, "medium", "Non-clustered index stores?","Actual data","Pointers to data","Only keys","Temp table","b","Non-clustered index stores pointers to rows.","sql,indexing"),
(sql_id, sql_indexing_id, "medium", "Too many indexes cause?","Faster reads","Slower writes","Better joins","No effect","b","Indexes slow down insert/update operations.","sql,indexing"),
(sql_id, sql_indexing_id, "medium", "Index on low cardinality column?","Good","Bad","No effect","Always best","b","Low cardinality columns don't benefit much.","sql,indexing"),
(sql_id, sql_indexing_id, "medium", "Which column best for index?","Random column","Frequently filtered column","Large text column","Unused column","b","Indexes should be on frequently queried columns.","sql,indexing"),
(sql_id, sql_indexing_id, "medium", "Composite index used for?","Single column","Multiple columns","Only joins","Sorting","b","Composite index covers multiple columns.","sql,indexing"),
(sql_id, sql_indexing_id, "hard", "Query slow on WHERE name LIKE '%abc'?","Add index","Index not useful","Use join","Use group","b","Leading wildcard prevents index usage.","sql,indexing"),
(sql_id, sql_indexing_id, "hard", "ORDER BY slow query fix?","Remove order","Add index on column","Use join","Use group","b","Index helps sorting operations.","sql,indexing"),
(sql_id, sql_indexing_id, "hard", "JOIN slow on large tables?","Ignore","Index join columns","Delete data","Use subquery","b","Indexes on join columns improve performance.","sql,indexing"),
(sql_id, sql_indexing_id, "hard", "Full table scan happens when?","Index exists","No index or not used","Join present","Group used","b","Without proper index DB scans entire table.","sql,indexing"),
(sql_id, sql_indexing_id, "hard", "Index not used when?","Exact match","Function on column","Equality check","Join condition","b","Functions prevent index usage.","sql,indexing"),
(sql_id, sql_indexing_id, "medium", "Covering index means?","Full table copy","Index contains all needed columns","Primary key","Unique index","b","Query satisfied using index only.","sql,indexing"),
(sql_id, sql_indexing_id, "medium", "Best index for range queries?","Hash index","B-tree index","No index","Bitmap","b","B-tree supports range queries efficiently.","sql,indexing"),
(sql_id, sql_indexing_id, "medium", "Why avoid indexing every column?","Costly","Memory + slower writes","No benefit","Syntax error","b","Indexes increase storage and slow writes.","sql,indexing"),
(sql_id, sql_indexing_id, "hard", "E-commerce: search by user_id frequently?","No index","Index user_id","Delete data","Join only","b","Frequent filters need indexing.","sql,indexing"),
(sql_id, sql_indexing_id, "hard", "Analytics query scanning millions rows?","Ignore","Add proper indexes","Delete rows","Use loops","b","Indexes reduce scan cost significantly.","sql,indexing"),


# ── SQL QUERY OPTIMIZATION (REAL-WORLD) ──


(sql_id, sql_optimization_id, "easy", "What is query optimization?","Writing long queries","Improving query performance","Deleting data","Indexing only","b","Query optimization improves execution efficiency.","sql,optimization"),
(sql_id, sql_optimization_id, "easy", "Which tool analyzes query plan?","JOIN","EXPLAIN","GROUP BY","INDEX","b","EXPLAIN shows execution plan.","sql,optimization"),
(sql_id, sql_optimization_id, "easy", "What causes slow queries?","Indexes","Large data + bad queries","Small tables","Sorting","b","Poor design and large data slow queries.","sql,optimization"),
(sql_id, sql_optimization_id, "easy", "SELECT * impact?","Faster","Slower","No effect","Error","b","Fetching unnecessary columns slows queries.","sql,optimization"),
(sql_id, sql_optimization_id, "easy", "Best practice for columns?","Select all","Select required only","Random","Ignore","b","Fetch only needed columns.","sql,optimization"),
(sql_id, sql_optimization_id, "medium", "JOIN vs subquery performance?","Same","JOIN usually faster","Subquery always faster","Depends always","b","JOINs are often optimized better.","sql,optimization"),
(sql_id, sql_optimization_id, "medium", "Filter early or late?","Late","Early","Same","Never","b","Filtering early reduces data processing.","sql,optimization"),
(sql_id, sql_optimization_id, "medium", "What is full table scan?","Index scan","Scan entire table","Join scan","Group scan","b","Occurs when no index used.","sql,optimization"),
(sql_id, sql_optimization_id, "medium", "LIMIT helps performance?","No","Yes","Only sorting","Only joins","b","LIMIT reduces result size.","sql,optimization"),
(sql_id, sql_optimization_id, "medium", "Why avoid nested queries?","Hard to read","Slower execution","Both","None","c","Nested queries impact readability and performance.","sql,optimization"),
(sql_id, sql_optimization_id, "hard", "Slow GROUP BY fix?","Remove group","Add index on grouped column","Delete data","Use join","b","Index improves grouping performance.","sql,optimization"),
(sql_id, sql_optimization_id, "hard", "WHERE vs HAVING?","Same","HAVING faster","WHERE filters earlier","No diff","c","WHERE filters before aggregation.","sql,optimization"),
(sql_id, sql_optimization_id, "hard", "ORDER BY slow fix?","Remove order","Index column","Use join","Group data","b","Index helps sorting.","sql,optimization"),
(sql_id, sql_optimization_id, "hard", "Large OFFSET issue?","No issue","Slow scanning","Faster","Error","b","OFFSET requires skipping rows → slow.","sql,optimization"),
(sql_id, sql_optimization_id, "hard", "Pagination best approach?","OFFSET","Keyset pagination","Join","Group","b","Keyset pagination is faster for large data.","sql,optimization"),
(sql_id, sql_optimization_id, "medium", "Function in WHERE impact?","Faster","Index not used","No effect","Error","b","Functions prevent index usage.","sql,optimization"),
(sql_id, sql_optimization_id, "medium", "UNION vs UNION ALL?","Same","UNION ALL faster","UNION faster","No diff","b","UNION removes duplicates → slower.","sql,optimization"),
(sql_id, sql_optimization_id, "medium", "Denormalization used when?","Small DB","Performance needed","Testing","Debugging","b","Denormalization improves read performance.","sql,optimization"),
(sql_id, sql_optimization_id, "hard", "E-commerce slow search fix?","Ignore","Add index + optimize query","Delete data","Join only","b","Indexing + query tuning improves search.","sql,optimization"),
(sql_id, sql_optimization_id, "hard", "Dashboard slow queries fix?","Refresh page","Pre-aggregate data","Delete queries","Ignore","b","Pre-aggregation speeds dashboards.","sql,optimization"),


# ── DSA ARRAYS ──


(dsa_id, arrays_id, "easy", "What is an array?","Collection of random data","Collection of same type elements","Tree structure","Graph structure","b","Array stores same-type elements in contiguous memory.","dsa,arrays"),
(dsa_id, arrays_id, "easy", "Array indexing starts from?","1","0","-1","Depends","b","Arrays are 0-indexed in Python.","dsa,arrays"),
(dsa_id, arrays_id, "easy", "Time complexity of access by index?","O(n)","O(1)","O(log n)","O(n^2)","b","Direct index access is O(1).","dsa,arrays"),
(dsa_id, arrays_id, "easy", "What is linear search?","Binary search","Search one by one","Tree search","Graph search","b","Linear search checks each element.","dsa,arrays"),
(dsa_id, arrays_id, "easy", "Best case time of linear search?","O(n)","O(1)","O(log n)","O(n^2)","b","Best case when element is first.","dsa,arrays"),
(dsa_id, arrays_id, "medium", "What is time complexity of inserting at beginning?","O(1)","O(n)","O(log n)","O(n^2)","b","Shifting elements makes it O(n).","dsa,arrays"),
(dsa_id, arrays_id, "medium", "Difference array vs linked list?","Same","Array is contiguous memory","Linked list is faster access","No diff","b","Arrays use contiguous memory.","dsa,arrays"),
(dsa_id, arrays_id, "medium", "What is prefix sum?","Sorting","Cumulative sum array","Graph traversal","Tree method","b","Used for range sum queries.","dsa,arrays"),
(dsa_id, arrays_id, "medium", "Time complexity of finding max element?","O(1)","O(n)","O(log n)","O(n^2)","b","Need to scan all elements.","dsa,arrays"),
(dsa_id, arrays_id, "medium", "What is array rotation?","Sorting","Shifting elements","Deleting elements","Reversing string","b","Elements are shifted circularly.","dsa,arrays"),
(dsa_id, arrays_id, "hard", "Kadane’s algorithm is used for?","Sorting","Maximum subarray sum","Searching","Graph traversal","b","Finds max subarray sum efficiently.","dsa,arrays"),
(dsa_id, arrays_id, "hard", "Two sum optimal approach uses?","Loop","Hashing","Stack","Tree","b","Hash map reduces complexity to O(n).","dsa,arrays"),
(dsa_id, arrays_id, "hard", "Subarray vs subsequence difference?","Same","Subarray is continuous","Subsequence is random","No diff","b","Subarray must be contiguous.","dsa,arrays"),
(dsa_id, arrays_id, "hard", "Trapping rain water problem uses?","Sorting","Two pointers","DFS","Stack only","b","Two pointer technique is optimal.","dsa,arrays"),
(dsa_id, arrays_id, "hard", "Majority element problem optimal method?","Sorting","Moore Voting","Stack","Queue","b","Moore Voting algorithm works in O(n).","dsa,arrays"),
(dsa_id, arrays_id, "medium", "Best way to find duplicates?","Nested loop","Sorting","Hash set","Recursion","c","Set gives O(n) solution.","dsa,arrays"),
(dsa_id, arrays_id, "medium", "What is array space complexity?","O(1)","O(n)","O(log n)","O(n^2)","b","Array stores n elements.","dsa,arrays"),
(dsa_id, arrays_id, "medium", "What is stable array algorithm?","Preserves order","Random order","Faster sorting","Graph type","a","Stable keeps relative order.","dsa,arrays"),
(dsa_id, arrays_id, "hard", "Find missing number in array?","Sorting","Sum formula","DFS","Stack","b","Use n*(n+1)/2 formula.","dsa,arrays"),
(dsa_id, arrays_id, "hard", "Best approach for max product subarray?","Brute force","Track min & max","Sorting","Queue","b","Need both min and max tracking.","dsa,arrays"),


# ── DSA HASHING ──

(dsa_id, hashing_id, "easy", "What is the main purpose of hashing?", "Sorting data", "Fast lookup", "Tree traversal", "Recursion", "b", "Hashing is used for fast data retrieval using keys.", "dsa,hashing,basics"),
(dsa_id, hashing_id, "easy", "Average time complexity of hash table lookup?", "O(n)", "O(log n)", "O(1)", "O(n log n)", "c", "Hash tables provide average O(1) lookup time.", "dsa,hashing,complexity"),
(dsa_id, hashing_id, "easy", "Which data structure uses hashing internally in Python?", "List", "Tuple", "Dictionary", "Stack", "c", "Python dict uses hashing for key-value storage.", "dsa,hashing,python"),
(dsa_id, hashing_id, "easy", "What happens in hash collision?", "Error occurs", "Two keys map to same index", "Data deleted", "Sorting happens", "b", "Collision occurs when two keys map to same hash index.", "dsa,hashing,collision"),
(dsa_id, hashing_id, "medium", "How is collision handled in chaining?", "Sorting", "Linked list at index", "Binary tree", "Recursion", "b", "Chaining stores multiple values in a linked list at same index.", "dsa,hashing,collision"),
(dsa_id, hashing_id, "medium", "What is open addressing?", "External storage", "Find next empty slot", "Delete all duplicates", "Sort table", "b", "Open addressing resolves collision by probing next empty slot.", "dsa,hashing,collision"),
(dsa_id, hashing_id, "easy", "Which is best use case of hashing?", "Sorting array", "Searching elements quickly", "DFS traversal", "Graph coloring", "b", "Hashing is mainly used for fast search operations.", "dsa,hashing,usage"),
(dsa_id, hashing_id, "easy", "What is hash function?", "Sorting function", "Maps key to index", "Loop function", "Recursive function", "b", "Hash function converts key into array index.", "dsa,hashing,function"),
(dsa_id, hashing_id, "medium", "What is time complexity of worst-case hash lookup?", "O(1)", "O(log n)", "O(n)", "O(n log n)", "c", "Worst case occurs when all keys collide.", "dsa,hashing,complexity"),
(dsa_id, hashing_id, "medium", "Why is hash function important?", "Memory allocation", "Reduces collisions", "Increases loops", "Sorts data", "b", "Good hash function minimizes collisions.", "dsa,hashing,function"),
(dsa_id, hashing_id, "medium", "What is load factor in hashing?", "Size of array", "Ratio of elements to table size", "Number of keys", "Index value", "b", "Load factor = n / table size.", "dsa,hashing,performance"),
(dsa_id, hashing_id, "medium", "What happens if load factor increases too much?", "Faster search", "More collisions", "Less memory", "Sorting improves", "b", "High load factor increases collisions.", "dsa,hashing,performance"),
(dsa_id, hashing_id, "medium", "What is rehashing?", "Deleting data", "Increasing hash table size", "Sorting data", "Looping data", "b", "Rehashing resizes table and recomputes keys.", "dsa,hashing,optimization"),
(dsa_id, hashing_id, "easy", "Which DS is best for frequency counting?", "Stack", "Queue", "Hash map", "Tree", "c", "Hash map stores frequency efficiently.", "dsa,hashing,frequency"),
(dsa_id, hashing_id, "medium", "Real-world use of hashing?", "Sorting images", "Password storage", "Graph traversal", "Array reversal", "b", "Hashing is used in password hashing and security.", "dsa,hashing,realworld"),
(dsa_id, hashing_id, "medium", "What is purpose of hash set?", "Store duplicates", "Store unique values", "Sort values", "Tree structure", "b", "Hash set stores only unique elements.", "dsa,hashing,set"),
(dsa_id, hashing_id, "easy", "Which problem uses hashing heavily?", "Two sum", "Binary search", "Merge sort", "DFS", "a", "Two Sum is classic hashing problem.", "dsa,hashing,problem"),
(dsa_id, hashing_id, "medium", "Why hashing faster than array search?", "Sorted data", "Direct index mapping", "Recursion", "Trees", "b", "Hashing uses direct key-to-index mapping.", "dsa,hashing,performance"),
(dsa_id, hashing_id, "medium", "What is hashing drawback?", "Slow speed", "Collision handling complexity", "No memory use", "No search", "b", "Main issue is collision handling.", "dsa,hashing,limitation"),
(dsa_id, hashing_id, "hard", "Best technique for duplicate detection in large data?", "Sorting", "Hashing", "Recursion", "DFS", "b", "Hashing provides efficient duplicate detection.", "dsa,hashing,realworld"),


# ── DSA SLIDING WINDOW ──

(dsa_id, sliding_window_id, "easy", "What is sliding window technique used for?", "Sorting arrays", "Subarray/substring problems", "Graph traversal", "Tree traversal", "b", "Sliding window is used to solve subarray or substring problems efficiently.", "dsa,sliding_window,basics"),
(dsa_id, sliding_window_id, "easy", "Time complexity of sliding window approach?", "O(n²)", "O(n)", "O(log n)", "O(1)", "b", "Sliding window reduces nested loops to linear time O(n).", "dsa,sliding_window,complexity"),
(dsa_id, sliding_window_id, "easy", "Which problems use fixed-size sliding window?", "Tree traversal", "Maximum sum subarray of size k", "Sorting", "Recursion", "b", "Fixed window is used in problems like max sum subarray of size k.", "dsa,sliding_window,patterns"),
(dsa_id, sliding_window_id, "easy", "Which DS is often used with sliding window?", "Stack", "Queue/Deque", "Tree", "Graph", "b", "Deque is commonly used for efficient sliding window operations.", "dsa,sliding_window,ds"),
(dsa_id, sliding_window_id, "medium", "What is dynamic sliding window?", "Fixed size window", "Variable size window", "Sorting window", "Recursive window", "b", "Dynamic window expands and shrinks based on condition.", "dsa,sliding_window,patterns"),
(dsa_id, sliding_window_id, "medium", "Which problem uses variable window?", "Binary search", "Longest substring without repeating characters", "Sorting", "DFS", "b", "Variable window is used in longest substring problems.", "dsa,sliding_window,problem"),
(dsa_id, sliding_window_id, "easy", "What is sliding window optimization goal?", "Increase loops", "Avoid recomputation", "Sort data", "Use recursion", "b", "It avoids recomputing values again and again.", "dsa,sliding_window,optimization"),
(dsa_id, sliding_window_id, "medium", "What is brute force vs sliding window improvement?", "O(n²) → O(n)", "O(n) → O(n²)", "No change", "O(log n) → O(n)", "a", "Sliding window reduces nested loops to linear time.", "dsa,sliding_window,complexity"),
(dsa_id, sliding_window_id, "easy", "Which problem uses sliding window maximum?", "Stack problem", "Maximum in subarray", "Tree problem", "Graph shortest path", "b", "Used in maximum element in every window of size k.", "dsa,sliding_window,problem"),
(dsa_id, sliding_window_id, "medium", "Why deque is used in sliding window maximum?", "Sorting", "O(1) insertion/deletion", "Recursion", "Hashing", "b", "Deque helps maintain order efficiently.", "dsa,sliding_window,ds"),
(dsa_id, sliding_window_id, "medium", "What is window shrinking condition?", "When constraint violated", "Always grows", "Random", "Never shrinks", "a", "Window shrinks when condition is violated.", "dsa,sliding_window,logic"),
(dsa_id, sliding_window_id, "easy", "Sliding window is applied on?", "Graphs", "Arrays and Strings", "Trees only", "Heaps", "b", "It is mainly used on arrays and strings.", "dsa,sliding_window,basis"),
(dsa_id, sliding_window_id, "medium", "Which problem uses frequency map with sliding window?", "Binary tree", "Anagram search", "Sorting", "DFS", "b", "Frequency map is used in anagram detection.", "dsa,sliding_window,problem"),
(dsa_id, sliding_window_id, "medium", "What is condition for expanding window?", "Constraint satisfied", "Random choice", "Always shrink", "Depends on sorting", "a", "Window expands while condition is valid.", "dsa,sliding_window,logic"),
(dsa_id, sliding_window_id, "medium", "Real-world use of sliding window?", "Database indexing", "Network packet analysis", "Sorting numbers", "Tree traversal", "b", "Used in stream processing and network monitoring.", "dsa,sliding_window,realworld"),
(dsa_id, sliding_window_id, "easy", "What is fixed sliding window size?", "Variable", "Constant k", "Random", "Infinite", "b", "Window size remains constant k.", "dsa,sliding_window,types"),
(dsa_id, sliding_window_id, "medium", "Which technique often combines with sliding window?", "Recursion", "Hashing", "DFS", "Sorting only", "b", "Hashing is used for frequency tracking.", "dsa,sliding_window,hybrid"),
(dsa_id, sliding_window_id, "medium", "What is longest valid window problem?", "Shortest path", "Max valid substring", "Sorting", "Graph traversal", "b", "Find longest substring under constraint.", "dsa,sliding_window,problem"),
(dsa_id, sliding_window_id, "easy", "Sliding window avoids what?", "Loops", "Recomputation", "Memory", "Stack", "b", "It avoids recomputation of subarray results.", "dsa,sliding_window,optimization"),
(dsa_id, sliding_window_id, "hard", "Best case time improvement using sliding window?", "O(n²) to O(n)", "O(n) to O(log n)", "O(log n) to O(1)", "No improvement", "a", "Sliding window converts quadratic solutions into linear.", "dsa,sliding_window,complexity"),


# ── DSA TWO POINTERS ──

(dsa_id, two_pointers_id, "easy", "What is the two pointers technique used for?", "Sorting arrays", "Efficient traversal of arrays/strings", "Tree traversal", "Graph traversal", "b", "Two pointers is used to reduce time complexity in array and string problems.", "dsa,two_pointers,basics"),
(dsa_id, two_pointers_id, "easy", "Which data structure is commonly used with two pointers?", "Stack", "Array/String", "Graph", "Heap", "b", "Two pointers is mainly used on arrays and strings.", "dsa,two_pointers,ds"),
(dsa_id, two_pointers_id, "easy", "Time complexity of two pointers approach?", "O(n²)", "O(n)", "O(log n)", "O(1)", "b", "Two pointers typically reduce nested loops to O(n).", "dsa,two_pointers,complexity"),
(dsa_id, two_pointers_id, "easy", "Which problem uses two pointers commonly?", "Binary tree traversal", "Palindrome check", "Graph BFS", "Heap sort", "b", "Palindrome problems are classic two pointer use cases.", "dsa,two_pointers,problem"),
(dsa_id, two_pointers_id, "easy", "How do two pointers usually move?", "Randomly", "Same direction or opposite ends", "Only backward", "Only forward", "b", "Pointers move from both ends or same direction depending on problem.", "dsa,two_pointers,logic"),
(dsa_id, two_pointers_id, "medium", "Which problem uses opposite direction pointers?", "Stack problem", "Two sum in sorted array", "DFS", "Sorting", "b", "Sorted array two sum uses left-right pointers.", "dsa,two_pointers,problem"),
(dsa_id, two_pointers_id, "easy", "What is requirement for two pointers in sorted array problems?", "Unsorted array", "Sorted array", "Graph", "Tree", "b", "Sorted array helps compare and move pointers efficiently.", "dsa,two_pointers,requirement"),
(dsa_id, two_pointers_id, "medium", "Which problem uses fast and slow pointers?", "Binary search", "Cycle detection in linked list", "Sorting", "Heap", "b", "Floyd’s cycle detection uses fast and slow pointers.", "dsa,two_pointers,problem"),
(dsa_id, two_pointers_id, "medium", "Why is two pointers efficient?", "Uses recursion", "Reduces extra loops", "Uses hashing only", "Increases space", "b", "It avoids nested loops and reduces complexity.", "dsa,two_pointers,optimization"),
(dsa_id, two_pointers_id, "easy", "Which is a classic two pointers problem?", "Merge sort", "Remove duplicates from sorted array", "DFS traversal", "Heap insert", "b", "Removing duplicates uses two pointers.", "dsa,two_pointers,problem"),
(dsa_id, two_pointers_id, "medium", "What is sliding + two pointers combination used for?", "Sorting only", "Subarray problems", "Graph traversal", "Tree traversal", "b", "Used in longest substring and window problems.", "dsa,two_pointers,hybrid"),
(dsa_id, two_pointers_id, "easy", "Two pointers can be used on?", "Only trees", "Arrays and strings", "Graphs only", "Heaps only", "b", "Mostly used on arrays and strings.", "dsa,two_pointers,basis"),
(dsa_id, two_pointers_id, "medium", "What is left-right pointer technique used for?", "DFS", "Binary search only", "Pair finding problems", "Graph traversal", "c", "Used for pair-based searching in sorted arrays.", "dsa,two_pointers,pattern"),
(dsa_id, two_pointers_id, "medium", "Which problem uses shrinking window + two pointers?", "Heap sort", "Sliding window max", "Binary tree", "DFS", "b", "Window shrinking uses two pointers logic.", "dsa,two_pointers,hybrid"),
(dsa_id, two_pointers_id, "easy", "What is main benefit of two pointers?", "More memory", "Less time complexity", "More recursion", "Sorting improvement", "b", "It reduces time complexity significantly.", "dsa,two_pointers,benefit"),
(dsa_id, two_pointers_id, "medium", "Which problem uses three pointers sometimes?", "Binary tree", "Dutch national flag problem", "Heap sort", "DFS", "b", "Three pointers used for partitioning.", "dsa,two_pointers,advanced"),
(dsa_id, two_pointers_id, "easy", "What happens when condition fails in two pointers?", "Stop algorithm", "Move one pointer", "Delete array", "Restart program", "b", "Pointer movement depends on condition.", "dsa,two_pointers,logic"),
(dsa_id, two_pointers_id, "medium", "Which problem uses two pointers for merging?", "Merge two sorted arrays", "DFS", "Graph coloring", "Heap build", "a", "Merging sorted arrays uses two pointers.", "dsa,two_pointers,problem"),
(dsa_id, two_pointers_id, "medium", "What is space complexity of two pointers?", "O(n)", "O(1)", "O(log n)", "O(n²)", "b", "It uses constant extra space.", "dsa,two_pointers,complexity"),
(dsa_id, two_pointers_id, "hard", "Why is two pointers preferred over brute force?", "More memory", "Better scalability", "More loops", "Slower execution", "b", "It scales better for large inputs.", "dsa,two_pointers,optimization"),


# ── DSA STACK & QUEUE ──


(dsa_id, stack_queue_id, "easy", "What is a stack data structure?", "FIFO structure", "LIFO structure", "Random structure", "Tree structure", "b", "Stack follows Last In First Out (LIFO) principle.", "dsa,stack,basics"),
(dsa_id, stack_queue_id, "easy", "What is a queue data structure?", "LIFO structure", "FIFO structure", "Graph structure", "Tree structure", "b", "Queue follows First In First Out (FIFO) principle.", "dsa,queue,basics"),
(dsa_id, stack_queue_id, "easy", "Where is stack used in real systems?", "Database indexing", "Function call management", "Sorting", "Hashing", "b", "Stack is used for function calls and recursion.", "dsa,stack,realworld"),
(dsa_id, stack_queue_id, "easy", "Where is queue used in real systems?", "DFS traversal", "Task scheduling", "Sorting", "Recursion", "b", "Queue is used in scheduling and BFS.", "dsa,queue,realworld"),
(dsa_id, stack_queue_id, "easy", "Which operation adds element in stack?", "enqueue", "push", "insert front", "append left", "b", "push inserts element into stack.", "dsa,stack,operations"),
(dsa_id, stack_queue_id, "easy", "Which operation removes element from stack?", "pop", "dequeue", "delete", "remove first", "a", "pop removes top element from stack.", "dsa,stack,operations"),
(dsa_id, stack_queue_id, "easy", "Which operation inserts element in queue?", "push", "enqueue", "pop", "insert top", "b", "enqueue adds element to queue.", "dsa,queue,operations"),
(dsa_id, stack_queue_id, "easy", "Which operation removes element from queue?", "pop", "enqueue", "dequeue", "push", "c", "dequeue removes front element.", "dsa,queue,operations"),
(dsa_id, stack_queue_id, "medium", "What is stack overflow?", "Empty stack access", "Memory full stack", "Sorting error", "Graph loop", "b", "Occurs when stack exceeds memory limit.", "dsa,stack,errors"),
(dsa_id, stack_queue_id, "medium", "What is queue underflow?", "Empty queue removal", "Memory overflow", "Sorting error", "Deadlock", "a", "Occurs when removing from empty queue.", "dsa,queue,errors"),
(dsa_id, stack_queue_id, "easy", "Which DS is used in recursion?", "Queue", "Stack", "Heap", "Graph", "b", "Stack is used to manage recursive calls.", "dsa,stack,recursion"),
(dsa_id, stack_queue_id, "medium", "What is circular queue?", "Linear queue", "Queue with wrap-around", "Stack queue mix", "Tree queue", "b", "Circular queue reuses empty spaces.", "dsa,queue,advanced"),
(dsa_id, stack_queue_id, "medium", "Which problem uses stack for balancing?", "Binary search", "Balanced parentheses", "Graph traversal", "Sorting", "b", "Stack is used for matching brackets.", "dsa,stack,problem"),
(dsa_id, stack_queue_id, "medium", "Which DS is used in BFS?", "Stack", "Queue", "Heap", "Tree", "b", "BFS uses queue.", "dsa,queue,bfs"),
(dsa_id, stack_queue_id, "medium", "Which DS is used in DFS?", "Queue", "Stack", "Heap", "Graph only", "b", "DFS uses stack or recursion.", "dsa,stack,dfs"),
(dsa_id, stack_queue_id, "easy", "What is peek operation?", "Remove element", "View top/front element", "Insert element", "Sort elements", "b", "Peek returns top/front without removing.", "dsa,stack,queue,operations"),
(dsa_id, stack_queue_id, "medium", "Which problem uses monotonic stack?", "Sorting array", "Next greater element", "Binary search", "Graph traversal", "b", "Monotonic stack helps find next greater/smaller elements.", "dsa,stack,advanced"),
(dsa_id, stack_queue_id, "medium", "What is time complexity of stack operations?", "O(n)", "O(log n)", "O(1)", "O(n²)", "c", "Push and pop are O(1).", "dsa,stack,complexity"),
(dsa_id, stack_queue_id, "medium", "What is time complexity of queue operations?", "O(n)", "O(log n)", "O(1)", "O(n²)", "c", "Enqueue and dequeue are O(1).", "dsa,queue,complexity"),
(dsa_id, stack_queue_id, "hard", "Why is deque used in sliding window?", "Sorting", "Fast insert/delete both ends", "Recursion", "Graph traversal", "b", "Deque allows O(1) operations at both ends.", "dsa,queue,sliding_window"),


# ── DSA TREES ──


(dsa_id, trees_id, "easy", "What is a tree data structure?", "Linear structure", "Hierarchical structure", "Graph only", "Stack structure", "b", "Tree is a hierarchical data structure with parent-child relationships.", "dsa,trees,basics"),
(dsa_id, trees_id, "easy", "What is a root node?", "Leaf node", "Topmost node", "Middle node", "Last node", "b", "Root is the topmost node of a tree.", "dsa,trees,terminology"),
(dsa_id, trees_id, "easy", "What is a leaf node?", "Node with children", "Node with no children", "Root node", "Parent node", "b", "Leaf node has no children.", "dsa,trees,terminology"),
(dsa_id, trees_id, "easy", "What is height of a tree?", "Number of nodes", "Longest path from root to leaf", "Number of edges only", "Depth of leaf only", "b", "Height is longest root-to-leaf path.", "dsa,trees,concept"),
(dsa_id, trees_id, "easy", "What is binary tree?", "Tree with max 2 children", "Tree with 3 children", "Graph", "Queue", "a", "Binary tree has at most two children per node.", "dsa,trees,basics"),
(dsa_id, trees_id, "easy", "What is traversal?", "Deleting nodes", "Visiting nodes", "Sorting tree", "Balancing tree", "b", "Traversal means visiting all nodes.", "dsa,trees,traversal"),
(dsa_id, trees_id, "easy", "Which are tree traversals?", "DFS, BFS", "Sort, Search", "Push, Pop", "Map, Filter", "a", "DFS and BFS are tree traversal methods.", "dsa,trees,traversal"),
(dsa_id, trees_id, "easy", "Which is preorder traversal order?", "Left Root Right", "Root Left Right", "Right Left Root", "Random", "b", "Preorder is Root → Left → Right.", "dsa,trees,traversal"),
(dsa_id, trees_id, "easy", "Which is inorder traversal order?", "Root Left Right", "Left Root Right", "Right Root Left", "Level Order", "b", "Inorder is Left → Root → Right.", "dsa,trees,traversal"),
(dsa_id, trees_id, "easy", "Which is postorder traversal order?", "Root Left Right", "Left Right Root", "Right Left Root", "Level Order", "b", "Postorder is Left → Right → Root.", "dsa,trees,traversal"),
(dsa_id, trees_id, "easy", "Which traversal uses queue?", "DFS", "BFS", "Inorder", "Postorder", "b", "BFS uses queue (level order traversal).", "dsa,trees,bfs"),
(dsa_id, trees_id, "medium", "Which traversal uses stack?", "BFS", "DFS", "Level order", "None", "b", "DFS uses stack or recursion.", "dsa,trees,dfs"),
(dsa_id, trees_id, "medium", "What is binary search tree (BST)?", "Unordered tree", "Left < Root < Right", "Graph", "Heap", "b", "BST maintains ordering property.", "dsa,trees,bst"),
(dsa_id, trees_id, "medium", "Search in BST complexity?", "O(n)", "O(log n)", "O(n²)", "O(1)", "b", "Balanced BST gives O(log n) search.", "dsa,trees,bst"),
(dsa_id, trees_id, "medium", "What is level order traversal?", "DFS", "BFS by levels", "Sorting", "Recursion", "b", "Level order visits nodes level by level.", "dsa,trees,bfs"),
(dsa_id, trees_id, "medium", "Which DS is used in BFS tree traversal?", "Stack", "Queue", "Heap", "Graph", "b", "Queue is used in BFS.", "dsa,trees,bfs"),
(dsa_id, trees_id, "medium", "What is LCA in tree?", "Largest child", "Lowest Common Ancestor", "Leaf count", "Longest path", "b", "LCA is lowest common ancestor of two nodes.", "dsa,trees,advanced"),
(dsa_id, trees_id, "medium", "What is balanced tree?", "Random height", "Height difference small", "No root", "Only leaves", "b", "Balanced tree keeps height minimal.", "dsa,trees,balanced"),
(dsa_id, trees_id, "hard", "Worst case BST search complexity?", "O(1)", "O(log n)", "O(n)", "O(n log n)", "c", "Skewed BST becomes linked list.", "dsa,trees,bst"),
(dsa_id, trees_id, "medium", "Where are trees used in real world?", "Databases & file systems", "Sorting only", "Loops", "Stacks", "a", "Trees are used in DB indexes and file systems.", "dsa,trees,realworld"),


# ── DSA GRAPHS ──


(dsa_id, graphs_id, "easy", "What is a graph in DSA?", "Linear structure", "Collection of nodes and edges", "Stack structure", "Tree only", "b", "A graph consists of nodes (vertices) connected by edges.", "dsa,graphs,basics"),
(dsa_id, graphs_id, "easy", "What are nodes in a graph called?", "Vertices", "Edges", "Leaves", "Roots", "a", "Nodes are called vertices in graph terminology.", "dsa,graphs,terminology"),
(dsa_id, graphs_id, "easy", "What connects two nodes in a graph?", "Vertex", "Edge", "Pointer", "Link list", "b", "Edges connect two vertices.", "dsa,graphs,terminology"),
(dsa_id, graphs_id, "easy", "What is adjacency list?", "Matrix form", "List of connected nodes", "Sorted array", "Stack", "b", "Adjacency list stores neighbors of each node.", "dsa,graphs,representation"),
(dsa_id, graphs_id, "easy", "What is adjacency matrix?", "List representation", "2D matrix representation", "Tree structure", "Heap structure", "b", "Adjacency matrix uses 2D array to represent graph.", "dsa,graphs,representation"),
(dsa_id, graphs_id, "easy", "Which is more space efficient?", "Adjacency matrix", "Adjacency list", "Both same", "Depends on graph only", "b", "Adjacency list is more space efficient for sparse graphs.", "dsa,graphs,efficiency"),
(dsa_id, graphs_id, "easy", "What is a directed graph?", "Edges have direction", "No edges", "Only tree", "Undirected only", "a", "Directed graph has one-way edges.", "dsa,graphs,types"),
(dsa_id, graphs_id, "easy", "What is an undirected graph?", "One-way edges", "Two-way edges", "No edges", "Tree only", "b", "Edges can be traversed both directions.", "dsa,graphs,types"),
(dsa_id, graphs_id, "easy", "What is BFS?", "Depth traversal", "Breadth First Search", "Sorting", "Recursion only", "b", "BFS explores level by level.", "dsa,graphs,bfs"),
(dsa_id, graphs_id, "easy", "What data structure does BFS use?", "Stack", "Queue", "Heap", "Array", "b", "BFS uses queue.", "dsa,graphs,bfs"),
(dsa_id, graphs_id, "easy", "What is DFS?", "Level traversal", "Depth First Search", "Sorting", "Hashing", "b", "DFS explores depth before backtracking.", "dsa,graphs,dfs"),
(dsa_id, graphs_id, "easy", "What data structure does DFS use?", "Queue", "Stack", "Heap", "Matrix", "b", "DFS uses stack or recursion.", "dsa,graphs,dfs"),
(dsa_id, graphs_id, "medium", "Time complexity of BFS?", "O(n)", "O(n + e)", "O(log n)", "O(n²)", "b", "BFS visits all nodes and edges.", "dsa,graphs,complexity"),
(dsa_id, graphs_id, "medium", "Time complexity of DFS?", "O(n)", "O(n + e)", "O(log n)", "O(n²)", "b", "DFS also visits all nodes and edges.", "dsa,graphs,complexity"),
(dsa_id, graphs_id, "medium", "What is cycle in graph?", "Self loop only", "Path that starts and ends at same node", "Tree structure", "Sorting loop", "b", "Cycle occurs when you revisit a node.", "dsa,graphs,cycles"),
(dsa_id, graphs_id, "medium", "Where is graph used in real world?", "File system", "Social networks", "Stack only", "Sorting arrays", "b", "Graphs are used in social networks and maps.", "dsa,graphs,realworld"),
(dsa_id, graphs_id, "medium", "What is weighted graph?", "All edges equal", "Edges have weights", "No edges", "Tree only", "b", "Weighted graph has cost on edges.", "dsa,graphs,types"),
(dsa_id, graphs_id, "medium", "What is shortest path problem?", "Find max path", "Find minimum distance", "Sort nodes", "Delete edges", "b", "Find minimum distance between nodes.", "dsa,graphs,shortest_path"),
(dsa_id, graphs_id, "medium", "Which algorithm finds shortest path in unweighted graph?", "DFS", "BFS", "Merge sort", "Binary search", "b", "BFS gives shortest path in unweighted graphs.", "dsa,graphs,shortest_path"),
(dsa_id, graphs_id, "hard", "Why BFS is better than DFS for shortest path?", "Uses less memory", "Explores level by level", "Faster recursion", "Uses sorting", "b", "BFS explores level-wise ensuring shortest path.", "dsa,graphs,intuition"),


# ── ML BASICS ──


(ml_id, ml_basics_id, "easy", "What is Machine Learning in simple terms?", "Rule-based programming", "Learning patterns from data", "Database management", "OS scheduling", "b", "ML is about learning patterns from data instead of hard-coded rules.", "ml,basics,intro"),
(ml_id, ml_basics_id, "easy", "Which is NOT a type of ML?", "Supervised", "Unsupervised", "Reinforcement", "Compilation Learning", "d", "Compilation learning is not a valid ML type.", "ml,basics"),
(ml_id, ml_basics_id, "easy", "What is supervised learning?", "No labels used", "Data with labels", "Only clustering", "Only rewards", "b", "Supervised learning uses labeled data.", "ml,basics"),
(ml_id, ml_basics_id, "easy", "Example of supervised learning?", "K-means", "Linear regression", "PCA", "Apriori", "b", "Linear regression is supervised learning.", "ml,basics"),
(ml_id, ml_basics_id, "easy", "What is unsupervised learning?", "Data with labels", "Data without labels", "Only prediction", "Only classification", "b", "Unsupervised learning uses unlabeled data.", "ml,basics"),
(ml_id, ml_basics_id, "easy", "Example of unsupervised learning?", "Logistic regression", "K-means clustering", "SVM", "Decision tree", "b", "K-means is clustering algorithm.", "ml,basics"),
(ml_id, ml_basics_id, "easy", "What is reinforcement learning?", "Learning from labels", "Learning via rewards", "Database learning", "Sorting learning", "b", "RL learns from reward/penalty feedback.", "ml,basics"),
(ml_id, ml_basics_id, "easy", "What is dataset?", "Model output", "Collection of data", "Algorithm", "Loss function", "b", "Dataset is collection of data used for training.", "ml,basics"),
(ml_id, ml_basics_id, "easy", "What is feature?", "Output variable", "Input variable", "Model", "Loss", "b", "Feature is input variable used for prediction.", "ml,basics"),
(ml_id, ml_basics_id, "easy", "What is label?", "Input data", "Output to predict", "Noise", "Feature", "b", "Label is output variable.", "ml,basics"),
(ml_id, ml_basics_id, "easy", "What is model in ML?", "Database", "Function mapping input to output", "Table", "Query", "b", "Model learns mapping from inputs to outputs.", "ml,basics"),
(ml_id, ml_basics_id, "easy", "What is training in ML?", "Testing model", "Learning from data", "Deleting data", "Sorting data", "b", "Training means learning patterns from data.", "ml,basics"),
(ml_id, ml_basics_id, "easy", "What is testing in ML?", "Model learning", "Evaluating model performance", "Data cleaning", "Feature creation", "b", "Testing evaluates model on unseen data.", "ml,basics"),
(ml_id, ml_basics_id, "easy", "What is overfitting?", "Model performs well everywhere", "Model memorizes training data", "Model ignores data", "Model deletes data", "b", "Overfitting = memorizing training data.", "ml,basics"),
(ml_id, ml_basics_id, "easy", "What is underfitting?", "Perfect model", "Model too simple", "Model too complex", "No training", "b", "Underfitting = model is too simple.", "ml,basics"),
(ml_id, ml_basics_id, "easy", "What is bias in ML?", "Random error", "Error from wrong assumptions", "Data size", "Accuracy", "b", "Bias is error from wrong assumptions.", "ml,basics"),
(ml_id, ml_basics_id, "easy", "What is variance in ML?", "Model stability", "Sensitivity to data changes", "Accuracy", "Loss", "b", "Variance measures sensitivity to data changes.", "ml,basics"),
(ml_id, ml_basics_id, "easy", "What is bias-variance tradeoff?", "Accuracy vs speed", "Underfit vs overfit balance", "Data vs model", "Train vs test", "b", "Tradeoff between bias and variance.", "ml,basics"),
(ml_id, ml_basics_id, "easy", "What is feature vector?", "Single value", "Collection of features", "Label", "Dataset", "b", "Feature vector = set of input features.", "ml,basics"),
(ml_id, ml_basics_id, "easy", "What is model training goal?", "Maximize error", "Minimize loss", "Increase dataset", "Sort data", "b", "Goal is to minimize loss function.", "ml,basics"),
(ml_id, ml_basics_id, "medium", "What is training dataset used for?", "Final evaluation", "Model learning", "Deployment", "Monitoring", "b", "Training dataset is used for learning patterns.", "ml,basics"),
(ml_id, ml_basics_id, "medium", "What is test dataset used for?", "Training", "Final evaluation", "Feature engineering", "Cleaning", "b", "Test set evaluates generalization.", "ml,basics"),
(ml_id, ml_basics_id, "medium", "What is validation set?", "Final test", "Hyperparameter tuning", "Data storage", "Noise removal", "b", "Validation is used for tuning models.", "ml,basics"),
(ml_id, ml_basics_id, "medium", "Why split data?", "Increase size", "Avoid overfitting", "Delete noise", "Sort data", "b", "Splitting helps generalization.", "ml,basics"),
(ml_id, ml_basics_id, "medium", "What is generalization?", "Training accuracy", "Performance on unseen data", "Model size", "Loss only", "b", "Generalization = performance on unseen data.", "ml,basics"),
(ml_id, ml_basics_id, "medium", "What is data leakage?", "Missing data", "Test data used in training", "Large dataset", "Noise", "b", "Leakage causes unrealistic performance.", "ml,basics"),
(ml_id, ml_basics_id, "medium", "What is ML pipeline?", "Single model", "End-to-end workflow", "Database", "API only", "b", "Pipeline automates ML workflow.", "ml,basics"),
(ml_id, ml_basics_id, "medium", "Why normalization needed?", "Increase size", "Scale features", "Delete features", "Sort data", "b", "Normalization scales features for better training.", "ml,basics"),
(ml_id, ml_basics_id, "medium", "What is feature scaling?", "Deleting features", "Normalizing values", "Sorting data", "Encoding labels", "b", "Feature scaling standardizes data range.", "ml,basics"),
(ml_id, ml_basics_id, "hard", "Real-world issue if model accuracy is high but fails in production?", "Overfitting", "Underfitting", "Data leakage or poor generalization", "Good model", "c", "Model is not generalizing to real-world data.", "ml,basics"),


# ── ML ALGORITHMS ─


(ml_id, ml_algorithms_id, 'easy', 'What is supervised learning?', 'Learning without labels', 'Learning with labeled data', 'Clustering data', 'Reinforcement only', 'b', 'Uses labeled data for training.', 'ml,algorithms,basics'),
(ml_id, ml_algorithms_id, 'easy', 'What is unsupervised learning?', 'Learning with labels', 'Learning without labels', 'Rule-based system', 'SQL training', 'b', 'Works on unlabeled data.', 'ml,algorithms,basics'),
(ml_id, ml_algorithms_id, 'easy', 'What is regression used for?', 'Classification', 'Predict continuous value', 'Clustering', 'Dimensionality reduction', 'b', 'Predicts continuous values.', 'ml,algorithms,regression'),
(ml_id, ml_algorithms_id, 'easy', 'What is classification used for?', 'Predict continuous value', 'Predict categories', 'Clustering', 'Optimization', 'b', 'Predicts discrete classes.', 'ml,algorithms,classification'),
(ml_id, ml_algorithms_id, 'medium', 'What is overfitting?', 'Model performs only on test data', 'Model memorizes training data', 'Model underfits', 'Model ignores data', 'b', 'Learns noise instead of pattern.', 'ml,algorithms,overfitting'),
(ml_id, ml_algorithms_id, 'medium', 'What is underfitting?', 'Model too complex', 'Model too simple', 'Model perfect', 'Model optimized', 'b', 'Fails to capture patterns.', 'ml,algorithms,underfitting'),
(ml_id, ml_algorithms_id, 'medium', 'What is bias in ML?', 'Wrong assumptions error', 'Random error', 'Data leakage', 'Noise only', 'a', 'Error from simplified assumptions.', 'ml,algorithms,bias'),
(ml_id, ml_algorithms_id, 'medium', 'What is variance in ML?', 'Model stability', 'Sensitivity to data changes', 'Accuracy', 'Loss function', 'b', 'Model changes with data.', 'ml,algorithms,variance'),
(ml_id, ml_algorithms_id, 'medium', 'What is bias-variance tradeoff?', 'Only bias matters', 'Only variance matters', 'Balance between both errors', 'No concept', 'c', 'Balance of underfit and overfit.', 'ml,algorithms,concept'),
(ml_id, ml_algorithms_id, 'easy',  'What is linear regression?', 'Classification model', 'Line-based prediction model', 'Clustering model', 'Tree model', 'b', 'Predicts using linear relation.', 'ml,algorithms,regression'),
(ml_id, ml_algorithms_id, 'easy',   'What is logistic regression used for?', 'Regression only', 'Classification', 'Clustering', 'Sorting', 'b', 'Used for classification.', 'ml,algorithms,classification'),
(ml_id, ml_algorithms_id, 'medium', 'What is gradient descent?', 'Sorting algorithm', 'Optimization method', 'Database query', 'Tree traversal', 'b', 'Minimizes loss function.', 'ml,algorithms,optimization'),
(ml_id, ml_algorithms_id, 'medium', 'What is learning rate?', 'Data size', 'Step size in training', 'Model accuracy', 'Feature count', 'b', 'Controls update step size.', 'ml,algorithms,optimization'),
(ml_id, ml_algorithms_id, 'medium', 'What is entropy?', 'Data size', 'Impurity measure', 'Accuracy', 'Loss function', 'b', 'Measures randomness.', 'ml,algorithms,tree'),
(ml_id, ml_algorithms_id, 'medium', 'What is information gain?', 'Data increase', 'Reduction in entropy', 'Accuracy', 'Feature count', 'b', 'Measures split quality.', 'ml,algorithms,tree'),
(ml_id, ml_algorithms_id, 'medium', 'What is random forest?', 'Single tree', 'Multiple decision trees', 'Linear model', 'Clustering model', 'b', 'Ensemble of trees.', 'ml,algorithms,ensemble'),
(ml_id, ml_algorithms_id, 'medium', 'What is ensemble learning?', 'Single model', 'Multiple models combined', 'Data cleaning', 'Feature scaling', 'b', 'Combines models.', 'ml,algorithms,ensemble'),
(ml_id, ml_algorithms_id, 'medium', 'What is k-means?', 'Classification', 'Clustering algorithm', 'Regression', 'Optimization', 'b', 'Unsupervised clustering.', 'ml,algorithms,clustering'),
(ml_id, ml_algorithms_id, 'medium', 'What is k in k-means?', 'Features', 'Number of clusters', 'Data size', 'Loss', 'b', 'Defines cluster count.', 'ml,algorithms,clustering'),
(ml_id, ml_algorithms_id, 'medium', 'What is PCA used for?', 'Classification', 'Dimensionality reduction', 'Regression', 'Sorting', 'b', 'Reduces features.', 'ml,algorithms,dimensionality'),
(ml_id, ml_algorithms_id, 'medium', 'What is SVM?', 'Sorting method', 'Classification algorithm', 'Database index', 'Clustering', 'b', 'Finds separating hyperplane.', 'ml,algorithms,svm'),
(ml_id, ml_algorithms_id, 'hard',   'What is kernel trick?', 'Data cleaning', 'Higher dimension mapping', 'Sorting', 'Feature removal', 'b', 'Maps to higher dimension.', 'ml,algorithms,svm'),
(ml_id, ml_algorithms_id, 'medium', 'What is Naive Bayes?', 'Regression', 'Probability-based classifier', 'Decision tree', 'Clustering', 'b', 'Based on Bayes theorem.', 'ml,algorithms,probability'),
(ml_id, ml_algorithms_id, 'medium', 'What is KNN?', 'Clustering only', 'Nearest neighbor method', 'Regression only', 'Tree model', 'b', 'Uses nearest points.', 'ml,algorithms,knn'),
(ml_id, ml_algorithms_id, 'medium', 'What is distance metric?', 'Loss function', 'Similarity measure', 'Accuracy', 'Bias', 'b', 'Measures closeness.', 'ml,algorithms,knn'),
(ml_id, ml_algorithms_id, 'medium', 'What is feature scaling?', 'Adding features', 'Normalizing values', 'Deleting data', 'Sorting data', 'b', 'Brings features to same scale.', 'ml,algorithms,preprocessing'),
(ml_id, ml_algorithms_id, 'medium', 'What is standardization?', '0-1 scaling', 'Mean 0 std 1 scaling', 'Sorting', 'Encoding', 'b', 'Normal distribution scaling.', 'ml,algorithms,preprocessing'),
(ml_id, ml_algorithms_id, 'medium', 'What is normalization?', 'Mean scaling', '0 to 1 scaling', 'Sorting', 'Encoding', 'b', 'Scales values between 0-1.', 'ml,algorithms,preprocessing'),


# ── ML METRICS ─


(ml_id, ml_metrics_id, 'easy', 'What is accuracy?', 'True predictions / total predictions', 'Only positive predictions', 'Only negatives', 'Random score', 'a', 'Measures overall correctness.', 'ml,metrics,classification'),
(ml_id, ml_metrics_id, 'easy', 'When is accuracy misleading?', 'Balanced dataset', 'Imbalanced dataset', 'Small dataset', 'Large dataset', 'b', 'Fails in imbalanced classes.', 'ml,metrics,classification'),
(ml_id, ml_metrics_id, 'easy', 'What is precision?', 'TP/(TP+FP)', 'TP/(TP+FN)', 'TN/(TN+FP)', 'FP/(TP+FP)', 'a', 'Measures correctness of positive predictions.', 'ml,metrics,classification'),
(ml_id, ml_metrics_id, 'easy', 'What is recall?', 'TP/(TP+FN)', 'TP/(TP+FP)', 'TN/(TN+FP)', 'FN/(TP+FP)', 'a', 'Measures how many positives were found.', 'ml,metrics,classification'),
(ml_id, ml_metrics_id, 'easy', 'What is F1 score?', 'Average of precision and recall', 'Sum of accuracy and recall', 'Only precision', 'Only recall', 'a', 'Harmonic mean of precision and recall.', 'ml,metrics,classification'),
(ml_id, ml_metrics_id, 'medium', 'When is recall important?', 'Spam detection', 'Fraud detection', 'Image resizing', 'Sorting data', 'b', 'Recall is critical when missing positives is costly.', 'ml,metrics,classification'),
(ml_id, ml_metrics_id, 'medium', 'When is precision important?', 'Fraud detection', 'Spam filtering', 'Medical diagnosis only', 'Regression', 'b', 'Precision matters when false positives are costly.', 'ml,metrics,classification'),
(ml_id, ml_metrics_id, 'medium', 'What is ROC curve?', 'Accuracy curve', 'TPR vs FPR curve', 'Loss curve', 'Error curve', 'b', 'Shows tradeoff between TPR and FPR.', 'ml,metrics,roc'),
(ml_id, ml_metrics_id, 'medium', 'What is AUC?', 'Area under curve', 'Accuracy score', 'Loss function', 'Error rate', 'a', 'Measures separability of classes.', 'ml,metrics,roc'),
(ml_id, ml_metrics_id, 'medium', 'What does high AUC mean?', 'Poor model', 'Good separability', 'Overfitting always', 'Underfitting', 'b', 'Model distinguishes classes well.', 'ml,metrics,roc'),
(ml_id, ml_metrics_id, 'easy', 'What is confusion matrix?', 'Loss function', 'Table of predictions', 'Graph', 'Model type', 'b', 'Shows TP, TN, FP, FN.', 'ml,metrics,classification'),
(ml_id, ml_metrics_id, 'easy', 'What is TP?', 'True Positive', 'Total Positive', 'Test Prediction', 'Training Point', 'a', 'Correct positive prediction.', 'ml,metrics,classification'),
(ml_id, ml_metrics_id, 'easy', 'What is FP?', 'False Positive', 'False Prediction', 'Feature Point', 'Final Prediction', 'a', 'Incorrect positive prediction.', 'ml,metrics,classification'),
(ml_id, ml_metrics_id, 'easy', 'What is FN?', 'False Negative', 'Final Negative', 'Feature Noise', 'Filtered Negative', 'a', 'Missed positive prediction.', 'ml,metrics,classification'),
(ml_id, ml_metrics_id, 'easy', 'What is TN?', 'True Negative', 'Test Negative', 'Training Noise', 'True Noise', 'a', 'Correct negative prediction.', 'ml,metrics,classification'),
(ml_id, ml_metrics_id, 'medium', 'What is log loss?', 'Accuracy measure', 'Probability error measure', 'Sorting metric', 'Distance metric', 'b', 'Measures uncertainty of probabilities.', 'ml,metrics,loss'),
(ml_id, ml_metrics_id, 'medium', 'When is log loss used?', 'Regression', 'Classification probabilities', 'Clustering', 'Sorting', 'b', 'Used in probabilistic classification.', 'ml,metrics,loss'),
(ml_id, ml_metrics_id, 'medium', 'What is MSE?', 'Mean Squared Error', 'Model Score Estimate', 'Mean Standard Error', 'Metric Stability Error', 'a', 'Average squared difference.', 'ml,metrics,regression'),
(ml_id, ml_metrics_id, 'medium', 'What is RMSE?', 'Root Mean Squared Error', 'Random Mean Square Error', 'Relative Metric Score Error', 'None', 'a', 'Square root of MSE.', 'ml,metrics,regression'),
(ml_id, ml_metrics_id, 'medium', 'When use MAE?', 'Outlier sensitive data', 'Robust to outliers', 'Classification only', 'Clustering only', 'b', 'Less sensitive to outliers.', 'ml,metrics,regression'),
(ml_id, ml_metrics_id, 'medium', 'What is R2 score?', 'Accuracy metric', 'Variance explained', 'Loss function', 'Error rate', 'b', 'Explains variance in data.', 'ml,metrics,regression'),
(ml_id, ml_metrics_id, 'medium', 'What does R2 = 1 mean?', 'Bad model', 'Perfect model', 'Random model', 'Overfitting always', 'b', 'Perfect fit.', 'ml,metrics,regression'),
(ml_id, ml_metrics_id, 'medium', 'What does R2 = 0 mean?', 'Perfect model', 'No predictive power', 'Overfitting', 'Error', 'b', 'Model is as good as mean.', 'ml,metrics,regression'),
(ml_id, ml_metrics_id, 'medium', 'What is adjusted R2?', 'Modified R2 penalizing features', 'Raw accuracy', 'Loss function', 'Clustering metric', 'a', 'Penalizes unnecessary features.', 'ml,metrics,regression'),
(ml_id, ml_metrics_id, 'medium', 'Why use cross-validation?', 'Increase data size', 'Better model evaluation', 'Reduce features', 'Train faster', 'b', 'Gives stable performance estimate.', 'ml,metrics,validation'),
(ml_id, ml_metrics_id, 'medium', 'What is k-fold CV?', 'Split into k parts', 'Merge datasets', 'Remove features', 'Sort data', 'a', 'Data split into k subsets.', 'ml,metrics,validation'),
(ml_id, ml_metrics_id, 'medium', 'What is stratified CV?', 'Random split', 'Preserves class distribution', 'Sorting method', 'Clustering', 'b', 'Maintains class ratio.', 'ml,metrics,validation'),
(ml_id, ml_metrics_id, 'hard', 'What is data leakage?', 'Better performance', 'Test data used in training', 'Feature scaling', 'Noise removal', 'b', 'Information from test leaks into training.', 'ml,metrics,problem'),
(ml_id, ml_metrics_id, 'hard', 'Why is leakage dangerous?', 'Improves model', 'Gives false high accuracy', 'Reduces training time', 'Improves recall', 'b', 'Leads to unrealistic performance.', 'ml,metrics,problem'),
(ml_id, ml_metrics_id, 'medium', 'Which metric for imbalanced data?', 'Accuracy', 'F1 score', 'MSE', 'R2', 'b', 'F1 handles imbalance better.', 'ml,metrics,classification'),


# ── ML FEATURE ENGINEERING ─


(ml_id, ml_feature_eng_id, 'easy', 'What is feature engineering?', 'Building models', 'Creating useful input features', 'Training dataset', 'Deploying model', 'b', 'Feature engineering creates better input features for ML models.', 'ml,feature_engineering,basics'),
(ml_id, ml_feature_eng_id, 'easy', 'Why is feature engineering important?', 'Increases dataset size', 'Improves model performance', 'Reduces storage', 'Speeds SQL queries', 'b', 'Better features improve model accuracy.', 'ml,feature_engineering,importance'),
(ml_id, ml_feature_eng_id, 'easy', 'What is one-hot encoding?', 'Converts numbers to text', 'Converts categories into binary vectors', 'Removes nulls', 'Sorts data', 'b', 'Represents categories as binary columns.', 'ml,feature_engineering,encoding'),
(ml_id, ml_feature_eng_id, 'easy', 'When is one-hot encoding used?', 'Continuous variables', 'Categorical variables', 'Time series only', 'Images only', 'b', 'Used for categorical data.', 'ml,feature_engineering,encoding'),
(ml_id, ml_feature_eng_id, 'easy', 'What is label encoding?', 'Converts text to numbers', 'Deletes categories', 'Scales data', 'Clusters data', 'a', 'Assigns numeric labels to categories.', 'ml,feature_engineering,encoding'),
(ml_id, ml_feature_eng_id, 'medium', 'What is scaling in ML?', 'Feature creation', 'Bringing values to same range', 'Removing columns', 'Adding noise', 'b', 'Scaling normalizes feature ranges.', 'ml,feature_engineering,scaling'),
(ml_id, ml_feature_eng_id, 'medium', 'Why is scaling needed?', 'Improves storage', 'Prevents bias in distance-based models', 'Speeds SQL queries', 'Reduces dataset size', 'b', 'Important for KNN, SVM, etc.', 'ml,feature_engineering,scaling'),
(ml_id, ml_feature_eng_id, 'medium', 'What is normalization?', 'Mean centering', 'Scaling 0 to 1 range', 'Sorting data', 'Encoding data', 'b', 'Scales values between 0 and 1.', 'ml,feature_engineering,scaling'),
(ml_id, ml_feature_eng_id, 'medium', 'What is standardization?', '0-1 scaling', 'Mean=0 std=1 scaling', 'Sorting', 'Clustering', 'b', 'Transforms data to standard normal distribution.', 'ml,feature_engineering,scaling'),
(ml_id, ml_feature_eng_id, 'medium', 'What is log transformation?', 'Feature deletion', 'Reducing skewness', 'Encoding categories', 'Sorting values', 'b', 'Reduces skewed distributions.', 'ml,feature_engineering,transformation'),
(ml_id, ml_feature_eng_id, 'medium', 'When is log transform used?', 'Symmetric data', 'Skewed data', 'Categorical data', 'Text data', 'b', 'Used for skewed distributions.', 'ml,feature_engineering,transformation'),
(ml_id, ml_feature_eng_id, 'medium', 'What is polynomial feature engineering?', 'Removing features', 'Creating interaction features', 'Encoding text', 'Clustering', 'b', 'Adds higher degree feature combinations.', 'ml,feature_engineering,polynomial'),
(ml_id, ml_feature_eng_id, 'medium', 'What are interaction features?', 'Independent features', 'Combined features', 'Removed features', 'Random features', 'b', 'Features created by combining variables.', 'ml,feature_engineering,interaction'),
(ml_id, ml_feature_eng_id, 'medium', 'What is binning?', 'Encoding text', 'Grouping continuous values into bins', 'Scaling data', 'Sorting data', 'b', 'Converts continuous to categorical ranges.', 'ml,feature_engineering,binning'),
(ml_id, ml_feature_eng_id, 'medium', 'Why use binning?', 'Reduce model size', 'Handle non-linearity', 'Increase noise', 'Remove data', 'b', 'Helps capture non-linear patterns.', 'ml,feature_engineering,binning'),
(ml_id, ml_feature_eng_id, 'medium', 'What is feature selection?', 'Creating features', 'Selecting important features', 'Encoding data', 'Scaling data', 'b', 'Chooses most relevant features.', 'ml,feature_engineering,selection'),
(ml_id, ml_feature_eng_id, 'medium', 'Why remove irrelevant features?', 'Increase accuracy', 'Reduce overfitting', 'Increase noise', 'Slow model', 'b', 'Reduces overfitting risk.', 'ml,feature_engineering,selection'),
(ml_id, ml_feature_eng_id, 'medium', 'What is multicollinearity?', 'Independent features', 'Highly correlated features', 'Missing data', 'Categorical data', 'b', 'Strong correlation between features.', 'ml,feature_engineering,problem'),
(ml_id, ml_feature_eng_id, 'medium', 'Why remove multicollinearity?', 'Improves interpretability', 'Increases dataset size', 'Speeds database', 'Adds noise', 'a', 'Helps model stability.', 'ml,feature_engineering,problem'),
(ml_id, ml_feature_eng_id, 'medium', 'What is PCA used for?', 'Feature scaling', 'Dimensionality reduction', 'Encoding', 'Sorting', 'b', 'Reduces feature dimensions.', 'ml,feature_engineering,pca'),
(ml_id, ml_feature_eng_id, 'medium', 'What is feature extraction?', 'Selecting features', 'Creating new features from raw data', 'Deleting features', 'Sorting features', 'b', 'Transforms raw data into features.', 'ml,feature_engineering,extraction'),
(ml_id, ml_feature_eng_id, 'medium', 'Example of feature extraction?', 'Removing nulls', 'TF-IDF from text', 'Sorting rows', 'Filtering columns', 'b', 'TF-IDF converts text to features.', 'ml,feature_engineering,text'),
(ml_id, ml_feature_eng_id, 'medium', 'What is TF-IDF used for?', 'Images', 'Text representation', 'Regression', 'Scaling', 'b', 'Represents importance of words.', 'ml,feature_engineering,text'),
(ml_id, ml_feature_eng_id, 'medium', 'What is feature leakage?', 'Good feature design', 'Test data information in training', 'Scaling error', 'Encoding issue', 'b', 'Leaks future info into training.', 'ml,feature_engineering,problem'),
(ml_id, ml_feature_eng_id, 'hard', 'Why is leakage dangerous?', 'Improves real performance', 'Gives false accuracy', 'Speeds training', 'Reduces memory', 'b', 'Leads to unrealistic results.', 'ml,feature_engineering,problem'),
(ml_id, ml_feature_eng_id, 'medium', 'What is target encoding?', 'Encoding labels with mean target', 'Removing target', 'Scaling target', 'Clustering target', 'a', 'Encodes categories using target stats.', 'ml,feature_engineering,encoding'),
(ml_id, ml_feature_eng_id, 'medium', 'When to use target encoding?', 'High cardinality categorical data', 'Numeric data', 'Images', 'Text only', 'a', 'Used for many categories.', 'ml,feature_engineering,encoding'),
(ml_id, ml_feature_eng_id, 'medium', 'What is time-based feature engineering?', 'Random features', 'Extracting time features', 'Removing time', 'Scaling data', 'b', 'Uses date/time patterns.', 'ml,feature_engineering,time'),
(ml_id, ml_feature_eng_id, 'medium', 'Example of time feature?', 'User ID', 'Day of week', 'Password', 'IP address', 'b', 'Extract features like day/month/hour.', 'ml,feature_engineering,time'),
(ml_id, ml_feature_eng_id, 'medium', 'What is domain knowledge in feature engineering?', 'Random guessing', 'Business-driven feature creation', 'Model training', 'Data deletion', 'b', 'Uses real-world understanding.', 'ml,feature_engineering,concept'),


# ── ML PIPELINES ──


(ml_id, ml_pipelines_id, "easy", "What is an ML pipeline?","Single model","Sequence of data processing and modeling steps","Database","Loop","b","ML pipeline chains preprocessing and modeling steps.","ml,pipelines"),
(ml_id, ml_pipelines_id, "easy", "Which library provides Pipeline in Python?","NumPy","Pandas","Scikit-learn","Matplotlib","c","sklearn.pipeline.Pipeline is used to build pipelines.","ml,pipelines"),
(ml_id, ml_pipelines_id, "easy", "What is the last step in sklearn Pipeline?","Scaler","Encoder","Estimator/model","Imputer","c","Last step must be an estimator.","ml,pipelines"),
(ml_id, ml_pipelines_id, "easy", "What does Pipeline prevent?","Overfitting","Data leakage","Underfitting","Slow training","b","Pipeline prevents data leakage by fitting only on training data.","ml,pipelines"),
(ml_id, ml_pipelines_id, "easy", "What is data leakage?","Missing data","Test data info leaks into training","Overfitting","None","b","Leakage causes overoptimistic model performance.","ml,pipelines"),
(ml_id, ml_pipelines_id, "easy", "What is StandardScaler?","Encodes labels","Scales features to mean=0 std=1","Imputes values","Selects features","b","StandardScaler standardizes features.","ml,pipelines"),
(ml_id, ml_pipelines_id, "easy", "What is MinMaxScaler?","Standardizes","Scales to 0-1 range","Encodes","Imputes","b","MinMaxScaler scales between 0 and 1.","ml,pipelines"),
(ml_id, ml_pipelines_id, "easy", "What is SimpleImputer?","Scales data","Fills missing values","Encodes categories","Selects features","b","SimpleImputer handles missing values.","ml,pipelines"),
(ml_id, ml_pipelines_id, "easy", "What is OneHotEncoder?","Scales data","Converts categories to binary columns","Imputes values","Selects features","b","OHE creates binary columns for each category.","ml,pipelines"),
(ml_id, ml_pipelines_id, "easy", "What is LabelEncoder?","Scales data","Converts labels to integers","Imputes values","Selects features","b","LabelEncoder maps categories to integers.","ml,pipelines"),
(ml_id, ml_pipelines_id, "medium", "When to use LabelEncoder vs OneHotEncoder?","Same","OHE for nominal, Label for ordinal","Label always","OHE always","b","OHE avoids ordinal assumption for nominal data.","ml,pipelines"),
(ml_id, ml_pipelines_id, "medium", "What is ColumnTransformer?","Model step","Applies different transformers to different columns","Scales all","Encodes all","b","ColumnTransformer handles mixed data types.","ml,pipelines"),
(ml_id, ml_pipelines_id, "medium", "What is fit_transform()?","Fits only","Transforms only","Fits and transforms together","Predicts","c","fit_transform fits on data then transforms it.","ml,pipelines"),
(ml_id, ml_pipelines_id, "medium", "Why call fit() only on training data?","Speed","Prevent test data leaking into scaler","Accuracy","Memory","b","Fitting on test data causes leakage.","ml,pipelines"),
(ml_id, ml_pipelines_id, "medium", "What is feature selection in pipeline?","Adding features","Removing irrelevant features","Encoding","Scaling","b","Feature selection removes low-importance features.","ml,pipelines"),
(ml_id, ml_pipelines_id, "medium", "What is SelectKBest?","Encoder","Selects top K features","Imputer","Scaler","b","SelectKBest selects K highest scoring features.","ml,pipelines"),
(ml_id, ml_pipelines_id, "medium", "What is cross_val_score with pipeline?","Overfits","Evaluates pipeline preventing leakage","Slower","Error","b","Pipeline in CV prevents leakage across folds.","ml,pipelines"),
(ml_id, ml_pipelines_id, "medium", "What is GridSearchCV?","Model only","Hyperparameter tuning with cross-validation","Feature selection","Encoding","b","GridSearchCV searches best hyperparameters.","ml,pipelines"),
(ml_id, ml_pipelines_id, "medium", "Can GridSearchCV be used with Pipeline?","No","Yes","Only sometimes","Depends","b","GridSearchCV works seamlessly with Pipeline.","ml,pipelines"),
(ml_id, ml_pipelines_id, "medium", "How to name steps in Pipeline?","Automatic","Tuple of name and estimator","List","Dictionary","b","Pipeline accepts list of (name, estimator) tuples.","ml,pipelines"),
(ml_id, ml_pipelines_id, "medium", "What is make_pipeline()?","Same as Pipeline","Creates pipeline without naming steps","Faster model","Feature selector","b","make_pipeline auto-names steps.","ml,pipelines"),
(ml_id, ml_pipelines_id, "hard", "Pipeline with GridSearch param naming?","model__param","param only","step.param","param__model","a","Use stepname__parameter format.","ml,pipelines"),
(ml_id, ml_pipelines_id, "hard", "What is RobustScaler?","Like StandardScaler","Scales using median, robust to outliers","Encodes","Imputes","b","RobustScaler handles outliers better.","ml,pipelines"),
(ml_id, ml_pipelines_id, "hard", "Production pipeline must include?","Only model","Preprocessing + model together","Only scaler","Only encoder","b","Production needs full preprocessing + model.","ml,pipelines"),
(ml_id, ml_pipelines_id, "hard", "Save pipeline using?","CSV","joblib or pickle","JSON","TXT","b","joblib/pickle serializes the whole pipeline.","ml,pipelines"),
(ml_id, ml_pipelines_id, "hard", "Custom transformer requires?","fit only","fit() and transform() methods","predict()","score()","b","Custom transformers need fit and transform.","ml,pipelines"),
(ml_id, ml_pipelines_id, "hard", "Pipeline predict() calls?","Only model","Transform all steps then predict","Only scaler","Fit again","b","predict applies all transforms then predicts.","ml,pipelines"),
(ml_id, ml_pipelines_id, "hard", "Imbalanced dataset in pipeline?","Ignore","Use SMOTE or class_weight","Delete minority","Add more features","b","Imbalance needs resampling or weighting.","ml,pipelines"),
(ml_id, ml_pipelines_id, "hard", "Text data pipeline includes?","Scaler only","TfidfVectorizer or CountVectorizer","OHE only","Imputer only","b","Text needs vectorization step.","ml,pipelines"),
(ml_id, ml_pipelines_id, "hard", "Real interview: why use pipeline over manual steps?","No reason","Prevents leakage, cleaner, production-ready","Faster only","Accuracy only","b","Pipelines ensure reproducibility and prevent leakage.","ml,pipelines"),


# ── ML MODEL EVALUATION ──


(ml_id, ml_model_eval_id, "easy", "What is model evaluation?","Training model","Measuring model performance on unseen data","Cleaning data","Feature selection","b","Evaluation measures how well model generalizes.","ml,evaluation"),
(ml_id, ml_model_eval_id, "easy", "What is train-test split?","Splitting features","Dividing data into training and testing sets","Scaling data","Encoding data","b","Train-test split prevents overfitting evaluation.","ml,evaluation"),
(ml_id, ml_model_eval_id, "easy", "Typical train-test split ratio?","50-50","70-30 or 80-20","90-10","60-40","b","80-20 is most common split ratio.","ml,evaluation"),
(ml_id, ml_model_eval_id, "easy", "What is accuracy?","Loss value","Correct predictions / total predictions","Training speed","Model size","b","Accuracy = correct/total predictions.","ml,evaluation"),
(ml_id, ml_model_eval_id, "easy", "When is accuracy misleading?","Always","Imbalanced datasets","Small datasets","Large datasets","b","Accuracy fails when classes are imbalanced.","ml,evaluation"),
(ml_id, ml_model_eval_id, "easy", "What is a confusion matrix?","Accuracy table","Table of TP FP TN FN","Loss function","Feature table","b","Confusion matrix shows prediction breakdown.","ml,evaluation"),
(ml_id, ml_model_eval_id, "easy", "What is precision?","TP/Total","TP/(TP+FP)","TP/(TP+FN)","TN/(TN+FP)","b","Precision = correct positives / all predicted positives.","ml,evaluation"),
(ml_id, ml_model_eval_id, "easy", "What is recall?","TP/(TP+FP)","TP/(TP+FN)","TN/(TN+FN)","FP/(FP+TN)","b","Recall = correct positives / all actual positives.","ml,evaluation"),
(ml_id, ml_model_eval_id, "easy", "What is F1 score?","Accuracy","Harmonic mean of precision and recall","Sum of precision and recall","Loss value","b","F1 balances precision and recall.","ml,evaluation"),
(ml_id, ml_model_eval_id, "medium", "When to prefer recall over precision?","Spam detection","Cancer/fraud detection","Image classification","Sentiment analysis","b","High recall minimizes false negatives in critical cases.","ml,evaluation"),
(ml_id, ml_model_eval_id, "medium", "When to prefer precision over recall?","Cancer detection","Spam detection","Fraud detection","Churn detection","b","High precision minimizes false positives in spam.","ml,evaluation"),
(ml_id, ml_model_eval_id, "medium", "What is ROC curve?","Loss curve","True positive rate vs false positive rate curve","Accuracy curve","Feature curve","b","ROC plots TPR vs FPR at different thresholds.","ml,evaluation"),
(ml_id, ml_model_eval_id, "medium", "What is AUC?","Accuracy","Area under ROC curve","Loss value","Precision value","b","AUC measures overall model discrimination ability.","ml,evaluation"),
(ml_id, ml_model_eval_id, "medium", "AUC of 0.5 means?","Perfect model","Random model","Bad model","Good model","b","AUC 0.5 means model is no better than random.","ml,evaluation"),
(ml_id, ml_model_eval_id, "medium", "AUC of 1.0 means?","Random","Perfect classifier","Overfitting","Underfitting","b","AUC 1.0 means perfect classification.","ml,evaluation"),
(ml_id, ml_model_eval_id, "medium", "What is cross-validation?","Single train-test split","Multiple train-test splits for robust evaluation","Feature selection","Scaling","b","CV gives more reliable performance estimate.","ml,evaluation"),
(ml_id, ml_model_eval_id, "medium", "What is K-fold cross-validation?","K random splits","Data split into K folds, each used as test once","K models","K features","b","K-fold rotates test set across K folds.","ml,evaluation"),
(ml_id, ml_model_eval_id, "medium", "What is stratified K-fold?","Random split","Maintains class distribution in each fold","Faster split","Larger split","b","Stratified K-fold preserves class balance.","ml,evaluation"),
(ml_id, ml_model_eval_id, "medium", "What is MAE?","Classification metric","Mean Absolute Error for regression","Accuracy variant","AUC variant","b","MAE measures average absolute prediction error.","ml,evaluation"),
(ml_id, ml_model_eval_id, "medium", "What is RMSE?","Classification metric","Root Mean Squared Error","Accuracy variant","Precision variant","b","RMSE penalizes large errors more than MAE.","ml,evaluation"),
(ml_id, ml_model_eval_id, "medium", "When use RMSE over MAE?","Always","When large errors are more costly","Never","Small datasets","b","RMSE is sensitive to outlier errors.","ml,evaluation"),
(ml_id, ml_model_eval_id, "medium", "What is R-squared?","Classification metric","Proportion of variance explained by model","Loss value","Accuracy","b","R² measures goodness of fit in regression.","ml,evaluation"),
(ml_id, ml_model_eval_id, "hard", "Model high train accuracy low test accuracy?","Underfitting","Overfitting","Good model","Data issue","b","Gap between train and test = overfitting.","ml,evaluation"),
(ml_id, ml_model_eval_id, "hard", "Model low train and test accuracy?","Overfitting","Underfitting","Perfect model","Data leakage","b","Low on both = underfitting.","ml,evaluation"),
(ml_id, ml_model_eval_id, "hard", "Fraud detection: model shows 99% accuracy but fails. Why?","Good model","Imbalanced data - most transactions are legitimate","Overfitting","Wrong features","b","99% accuracy by predicting all as non-fraud on imbalanced data.","ml,evaluation"),
(ml_id, ml_model_eval_id, "hard", "Which metric for imbalanced classification?","Accuracy","F1 score or AUC","RMSE","MAE","b","F1/AUC handle imbalance better than accuracy.","ml,evaluation"),
(ml_id, ml_model_eval_id, "hard", "What is threshold tuning?","Feature selection","Adjusting classification cutoff for precision-recall tradeoff","Scaling","Encoding","b","Threshold adjusts sensitivity of classifier.","ml,evaluation"),
(ml_id, ml_model_eval_id, "hard", "Production model performance drops. First check?","Retrain immediately","Check for data drift","Delete model","Add features","b","Data drift causes production degradation.","ml,evaluation"),
(ml_id, ml_model_eval_id, "hard", "What is data drift?","Missing data","Input data distribution changes over time","Overfitting","Feature issue","b","Drift means real-world data changed from training data.","ml,evaluation"),
(ml_id, ml_model_eval_id, "hard", "Best evaluation strategy for time-series model?","Random K-fold","Time-based split — past trains future","Stratified K-fold","LOOCV","b","Future data must never train on past in time series.","ml,evaluation"),


# ── STATISTICS: PROBABILITY ──


(stats_id, probability_id, "easy", "What is probability?","Certainty","Likelihood of event between 0 and 1","Average","Standard deviation","b","Probability measures likelihood of an event occurring.","stats,probability"),
(stats_id, probability_id, "easy", "Probability of impossible event?","1","0.5","0","Infinity","c","Impossible event has probability 0.","stats,probability"),
(stats_id, probability_id, "easy", "Probability of certain event?","0","0.5","0.9","1","d","Certain event always has probability 1.","stats,probability"),
(stats_id, probability_id, "easy", "What is sample space?","Single outcome","All possible outcomes","Favorable outcomes","Mean value","b","Sample space contains all possible outcomes.","stats,probability"),
(stats_id, probability_id, "easy", "What is an event in probability?","Sample space","Subset of sample space","Mean","Variance","b","Event is a subset of the sample space.","stats,probability"),
(stats_id, probability_id, "easy", "P(A) + P(not A) = ?","0","0.5","1","2","c","Complementary probabilities sum to 1.","stats,probability"),
(stats_id, probability_id, "easy", "What is joint probability?","P(A) only","P(A and B)","P(A or B)","P(A given B)","b","Joint probability is P(A and B).","stats,probability"),
(stats_id, probability_id, "easy", "What is P(A or B) for mutually exclusive events?","P(A)*P(B)","P(A)+P(B)","P(A)-P(B)","P(A)/P(B)","b","Mutually exclusive: P(A or B) = P(A) + P(B).","stats,probability"),
(stats_id, probability_id, "easy", "What are mutually exclusive events?","Both can occur","Cannot occur together","Always occur together","Independent events","b","Mutually exclusive events cannot happen simultaneously.","stats,probability"),
(stats_id, probability_id, "medium", "What is conditional probability?","P(A)","P(A given B has occurred)","P(A and B)","P(A or B)","b","P(A|B) is probability of A given B occurred.","stats,probability"),
(stats_id, probability_id, "medium", "Formula for P(A|B)?","P(A)*P(B)","P(A and B)/P(B)","P(A)+P(B)","P(B)/P(A)","b","Conditional probability = joint/marginal.","stats,probability"),
(stats_id, probability_id, "medium", "What are independent events?","Cannot occur together","Occurrence of one does not affect other","Always occur together","Mutually exclusive","b","Independent events have no influence on each other.","stats,probability"),
(stats_id, probability_id, "medium", "For independent events P(A and B) = ?","P(A)+P(B)","P(A)*P(B)","P(A)-P(B)","P(A)/P(B)","b","Independent events multiply probabilities.","stats,probability"),
(stats_id, probability_id, "medium", "What is Bayes theorem used for?","Sorting data","Updating probability with new evidence","Scaling data","Feature selection","b","Bayes updates prior probability with new evidence.","stats,probability"),
(stats_id, probability_id, "medium", "What is prior probability?","Updated probability","Initial probability before evidence","Joint probability","Conditional probability","b","Prior is probability before observing evidence.","stats,probability"),
(stats_id, probability_id, "medium", "What is posterior probability?","Prior probability","Updated probability after evidence","Joint probability","Marginal probability","b","Posterior is updated belief after seeing evidence.","stats,probability"),
(stats_id, probability_id, "medium", "What is likelihood in Bayes?","Prior","P(evidence given hypothesis)","Posterior","Marginal","b","Likelihood measures how probable evidence is given hypothesis.","stats,probability"),
(stats_id, probability_id, "medium", "Naive Bayes assumes?","Dependent features","Independent features","Equal features","No features","b","Naive Bayes assumes feature independence.","stats,probability"),
(stats_id, probability_id, "medium", "What is expected value?","Most likely outcome","Weighted average of all outcomes","Median outcome","Mode outcome","b","Expected value is probability-weighted average.","stats,probability"),
(stats_id, probability_id, "medium", "Expected value formula?","Sum of outcomes","Sum of outcome * probability","Max outcome","Min outcome","b","E(X) = sum of x * P(x).","stats,probability"),
(stats_id, probability_id, "hard", "Email spam filter uses which theorem?","Central limit","Bayes theorem","Law of large numbers","Bernoulli","b","Spam filters apply Bayes to classify emails.","stats,probability"),
(stats_id, probability_id, "hard", "Medical test 99% accurate, disease rare 1%. Person tests positive. Probability actually sick?","99%","~50%","~9%","1%","c","Base rate fallacy - rare disease lowers actual probability.","stats,probability"),
(stats_id, probability_id, "hard", "What is the law of large numbers?","Small samples accurate","Sample mean approaches population mean with more data","Probability always 0.5","Events are independent","b","More data makes sample statistics more reliable.","stats,probability"),
(stats_id, probability_id, "hard", "What is Monte Carlo simulation?","Exact calculation","Random sampling to estimate probability","Sorting algorithm","Feature selection","b","Monte Carlo uses random samples for estimation.","stats,probability"),
(stats_id, probability_id, "hard", "Coin flipped 100 times, 60 heads. Is coin fair?","Yes definitely","Use hypothesis test to decide","No definitely","Cannot determine","b","Statistical test needed to determine fairness.","stats,probability"),
(stats_id, probability_id, "hard", "What is the birthday paradox?","23 people needed for 50% shared birthday chance","100 people needed","Impossible","Always true","a","Only 23 people needed for 50% probability of shared birthday.","stats,probability"),
(stats_id, probability_id, "hard", "Gambler's fallacy is?","Correct probability thinking","Believing past outcomes affect independent future events","Law of large numbers","Bayes theorem","b","Past coin flips don't affect future independent flips.","stats,probability"),
(stats_id, probability_id, "hard", "What is regression to mean?","Overfitting","Extreme values tend toward average over time","Data cleaning","Feature selection","b","Extreme results naturally move toward average over time.","stats,probability"),
(stats_id, probability_id, "hard", "Customer churn probability uses?","Sorting","Logistic regression with probability output","Linear regression","Clustering","b","Logistic regression outputs churn probability.","stats,probability"),
(stats_id, probability_id, "hard", "What is selection bias?","Random sampling","Non-random sampling causing skewed results","Data cleaning","Feature engineering","b","Selection bias skews results due to non-random sampling.","stats,probability"),


# ── STATISTICS: DISTRIBUTIONS ──


(stats_id, distributions_id, "easy", "What is a probability distribution?","Single value","Shows all possible values and their probabilities","Average only","Sorted data","b","Distribution shows probability of each possible outcome.","stats,distributions"),
(stats_id, distributions_id, "easy", "What is normal distribution?","Skewed distribution","Bell-shaped symmetric distribution","Uniform distribution","Bimodal distribution","b","Normal distribution is symmetric bell-shaped curve.","stats,distributions"),
(stats_id, distributions_id, "easy", "Normal distribution is defined by?","Mean only","Mean and standard deviation","Median and mode","Min and max","b","Normal distribution needs mean and standard deviation.","stats,distributions"),
(stats_id, distributions_id, "easy", "What is uniform distribution?","Bell shaped","All outcomes equally likely","Skewed right","Skewed left","b","Uniform distribution has equal probability for all values.","stats,distributions"),
(stats_id, distributions_id, "easy", "What is binomial distribution?","Continuous outcomes","Fixed trials with two outcomes","Normal distribution","Uniform distribution","b","Binomial models success/failure in fixed number of trials.","stats,distributions"),
(stats_id, distributions_id, "easy", "What is Poisson distribution?","Binary outcomes","Count of events in fixed time/space","Normal distribution","Uniform distribution","b","Poisson models count of rare events in fixed interval.","stats,distributions"),
(stats_id, distributions_id, "easy", "68-95-99.7 rule applies to?","Uniform","Normal distribution","Binomial","Poisson","b","68-95-99.7 rule describes standard deviation ranges in normal distribution.","stats,distributions"),
(stats_id, distributions_id, "easy", "What percentage of data falls within 1 standard deviation?","50%","68%","95%","99.7%","b","68% of data lies within 1 SD in normal distribution.","stats,distributions"),
(stats_id, distributions_id, "easy", "What is skewness?","Spread of data","Measure of asymmetry of distribution","Central tendency","Variation","b","Skewness measures how asymmetric a distribution is.","stats,distributions"),
(stats_id, distributions_id, "easy", "Right skewed distribution has?","Mean less than median","Mean greater than median","Mean equals median","No tail","b","Right skew pulls mean above median.","stats,distributions"),
(stats_id, distributions_id, "medium", "What is kurtosis?","Skewness","Measure of tail heaviness","Central tendency","Variance","b","Kurtosis measures how heavy the tails are.","stats,distributions"),
(stats_id, distributions_id, "medium", "What is a Z-score?","Raw value","Number of standard deviations from mean","Probability","Variance","b","Z-score standardizes values relative to mean.","stats,distributions"),
(stats_id, distributions_id, "medium", "Z-score formula?","(x-mean)/std","(x+mean)/std","x*std","x/mean","a","Z = (value - mean) / standard deviation.","stats,distributions"),
(stats_id, distributions_id, "medium", "What is central limit theorem?","Small samples normal","Sample means approach normal distribution with large n","All data normal","Median theorem","b","CLT ensures sample means are normally distributed.","stats,distributions"),
(stats_id, distributions_id, "medium", "CLT requires sample size?","n=5","n=10","n>=30 generally","n=100","c","Sample size of 30+ typically satisfies CLT.","stats,distributions"),
(stats_id, distributions_id, "medium", "What is exponential distribution?","Binary outcomes","Time between events","Count of events","Normal variant","b","Exponential models time between Poisson events.","stats,distributions"),
(stats_id, distributions_id, "medium", "What is log-normal distribution?","Normal data","Data whose log is normally distributed","Uniform variant","Binomial variant","b","Log-normal used for skewed positive data like income.","stats,distributions"),
(stats_id, distributions_id, "medium", "Which distribution for binary classification probability?","Normal","Bernoulli","Poisson","Uniform","b","Bernoulli models single binary outcome.","stats,distributions"),
(stats_id, distributions_id, "medium", "Which distribution for click-through rates?","Normal","Binomial","Poisson","Exponential","b","Binomial models success/failure across trials.","stats,distributions"),
(stats_id, distributions_id, "medium", "Website traffic per hour follows?","Normal","Binomial","Poisson","Uniform","c","Poisson models count of events per unit time.","stats,distributions"),
(stats_id, distributions_id, "hard", "Income distribution is typically?","Normal","Right skewed","Left skewed","Uniform","b","Income is right skewed - few earn very high.","stats,distributions"),
(stats_id, distributions_id, "hard", "Which transform reduces right skew?","Square","Log transform","Sqrt only","Inverse","b","Log transform reduces right skewness.","stats,distributions"),
(stats_id, distributions_id, "hard", "What is QQ plot used for?","Sorting","Checking if data follows a distribution","Feature selection","Model evaluation","b","QQ plot compares data to theoretical distribution.","stats,distributions"),
(stats_id, distributions_id, "hard", "Product defect rate per 1000 units uses?","Normal","Binomial","Poisson","Uniform","c","Poisson models rare events per fixed unit.","stats,distributions"),
(stats_id, distributions_id, "hard", "What is heavy tail distribution?","Normal","Distribution with extreme values more likely than normal","Uniform","Binomial","b","Heavy tails mean more extreme outliers.","stats,distributions"),
(stats_id, distributions_id, "hard", "Stock returns distribution?","Perfectly normal","Approximately normal with heavy tails","Uniform","Binomial","b","Stock returns show fat tails not pure normal.","stats,distributions"),
(stats_id, distributions_id, "hard", "What is mixture distribution?","Single distribution","Combination of multiple distributions","Uniform","Poisson variant","b","Mixture combines multiple component distributions.","stats,distributions"),
(stats_id, distributions_id, "hard", "When to use non-parametric test?","Always","Data doesn't follow known distribution","Data is normal","Large sample","b","Non-parametric tests make no distribution assumptions.","stats,distributions"),
(stats_id, distributions_id, "hard", "Multimodal distribution has?","One peak","Multiple peaks","No peak","Uniform shape","b","Multimodal distributions have multiple modes.","stats,distributions"),
(stats_id, distributions_id, "hard", "Which distribution models server response times?","Normal","Exponential or log-normal","Binomial","Uniform","b","Response times often follow exponential or log-normal.","stats,distributions"),


# ── STATISTICS: HYPOTHESIS TESTING ──


(stats_id, hypothesis_testing_id, "easy", "What is hypothesis testing?","Data cleaning","Statistical method to validate assumptions about population","Feature selection","Model training","b","Hypothesis testing validates statistical claims using data.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "easy", "What is null hypothesis?","Alternative claim","Default assumption of no effect","True hypothesis","Proven claim","b","Null hypothesis assumes no effect or difference exists.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "easy", "What is alternative hypothesis?","Default assumption","Claim we want to prove","Null hypothesis","Rejected claim","b","Alternative hypothesis is what we aim to support.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "easy", "What is p-value?","Model accuracy","Probability of results occurring by chance under null","Mean value","Standard deviation","b","P-value shows probability of observing results if null is true.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "easy", "Common significance level?","0.01","0.05","0.10","0.50","b","Alpha = 0.05 is most commonly used threshold.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "easy", "Reject null when p-value is?","Greater than alpha","Less than alpha","Equal to alpha","Zero","b","Reject null when p-value < significance level.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "easy", "What is Type I error?","Missing real effect","False positive - rejecting true null","Correct decision","Type II error","b","Type I error rejects a true null hypothesis.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "easy", "What is Type II error?","False positive","False negative - failing to reject false null","Correct rejection","Type I error","b","Type II error fails to reject a false null hypothesis.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "easy", "What is statistical power?","Type I error rate","Probability of correctly rejecting false null","P-value","Alpha","b","Power is probability of detecting a real effect.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "medium", "What is t-test used for?","Comparing variances","Comparing means of two groups","Correlation","Regression","b","T-test compares means between groups.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "medium", "What is one-sample t-test?","Compare two groups","Compare sample mean to known value","Compare variances","Correlation test","b","One-sample t-test compares sample to population mean.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "medium", "What is two-sample t-test?","Compare to fixed value","Compare means of two independent groups","Compare variances","Paired test","b","Two-sample t-test compares means of two groups.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "medium", "What is chi-square test?","Means comparison","Test for independence between categorical variables","Regression","Correlation","b","Chi-square tests relationship between categorical variables.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "medium", "What is ANOVA?","Two group comparison","Comparison of means across 3+ groups","Correlation test","Regression","b","ANOVA compares means across multiple groups.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "medium", "What is paired t-test used for?","Independent groups","Same group measured twice","Three groups","Categorical data","b","Paired t-test compares before and after measurements.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "medium", "Difference between one-tailed and two-tailed test?","Same","One-tailed tests direction, two-tailed tests any difference","Speed difference","P-value difference","b","One-tailed checks one direction, two-tailed checks both.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "medium", "What is confidence interval?","Single value estimate","Range likely containing true population parameter","P-value","Test statistic","b","CI gives range where true value likely falls.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "medium", "95% confidence interval means?","95% chance null rejected","If repeated 100 times, 95 CIs contain true value","95% accuracy","P-value 0.95","b","95% CI means 95 of 100 intervals capture true parameter.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "medium", "What is effect size?","P-value","Magnitude of difference between groups","Sample size","Test statistic","b","Effect size measures practical significance of difference.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "medium", "Large sample size affects p-value how?","No effect","Makes it easier to find significance","Harder to find significance","Increases effect size","b","Larger samples detect smaller differences as significant.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "hard", "Statistically significant but not practically significant?","Impossible","Small effect size with large sample","Always meaningful","Type I error","b","Large samples can make trivial differences significant.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "hard", "What is multiple testing problem?","Single test issue","Running many tests increases false positive rate","Power issue","Sample size issue","b","More tests increase chance of false positives.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "hard", "Bonferroni correction does?","Increases alpha","Divides alpha by number of tests","Increases power","Reduces sample size","b","Bonferroni adjusts significance level for multiple tests.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "hard", "What is p-hacking?","Valid analysis","Manipulating analysis until p<0.05","Type II error","Correct testing","b","P-hacking is cherry-picking results to get significance.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "hard", "A/B test shows p=0.04. What to conclude?","Definitely significant","Reject null at 0.05 level but consider practical significance","Accept null","No conclusion","b","Statistical significance found but check effect size too.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "hard", "New feature reduces churn. How to validate?","Trust result","Run hypothesis test on control vs treatment group","Use intuition","Check model accuracy","b","Hypothesis test validates if churn reduction is significant.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "hard", "What is Shapiro-Wilk test?","Variance test","Tests if data is normally distributed","Correlation test","Mean comparison","b","Shapiro-Wilk checks normality assumption.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "hard", "Non-parametric alternative to t-test?","ANOVA","Mann-Whitney U test","Chi-square","F-test","b","Mann-Whitney U is non-parametric alternative to t-test.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "hard", "What is bootstrap method?","Sorting","Resampling with replacement to estimate statistics","Feature selection","Model training","b","Bootstrap estimates uncertainty by resampling data.","stats,hypothesis"),
(stats_id, hypothesis_testing_id, "hard", "Marketing campaign effectiveness test uses?","Regression","Two-sample t-test or chi-square","Clustering","PCA","b","Compare conversion rates between campaign groups.","stats,hypothesis"),


# ── STATISTICS: A/B TESTING ──


(stats_id, ab_testing_id, "easy", "What is A/B testing?","Feature selection","Comparing two versions to determine which performs better","Data cleaning","Model training","b","A/B testing compares control vs treatment groups.","stats,abtesting"),
(stats_id, ab_testing_id, "easy", "What is control group in A/B test?","New version","Existing baseline version","Random group","Largest group","b","Control group receives existing version.","stats,abtesting"),
(stats_id, ab_testing_id, "easy", "What is treatment group?","Existing version","Group receiving new version","Random group","Smallest group","b","Treatment group receives the new variation.","stats,abtesting"),
(stats_id, ab_testing_id, "easy", "What metric is tested in A/B test?","Any random metric","Primary business metric like conversion rate","Only revenue","Only clicks","b","A/B tests focus on key business metrics.","stats,abtesting"),
(stats_id, ab_testing_id, "easy", "What statistical test is used in A/B testing?","Regression","Hypothesis test - t-test or chi-square","Clustering","PCA","b","Hypothesis tests determine if difference is significant.","stats,abtesting"),
(stats_id, ab_testing_id, "easy", "What is conversion rate?","Revenue","Percentage of users completing desired action","Click rate","Bounce rate","b","Conversion rate = conversions / total visitors.","stats,abtesting"),
(stats_id, ab_testing_id, "easy", "When to stop an A/B test?","Immediately","After reaching predetermined sample size","When p<0.05","After 1 week always","b","Stop after planned sample size to avoid peeking.","stats,abtesting"),
(stats_id, ab_testing_id, "easy", "What is statistical significance in A/B test?","Always true","Difference unlikely due to random chance","P-value > 0.05","Sample size","b","Significance means result is unlikely by chance.","stats,abtesting"),
(stats_id, ab_testing_id, "easy", "Minimum detectable effect means?","Maximum effect","Smallest effect worth detecting","Average effect","Zero effect","b","MDE is smallest meaningful business improvement.","stats,abtesting"),
(stats_id, ab_testing_id, "medium", "What is sample size calculation based on?","Guess","MDE, alpha, power, and baseline rate","Revenue only","Time only","b","Sample size needs MDE, significance level and power.","stats,abtesting"),
(stats_id, ab_testing_id, "medium", "What is peeking problem in A/B testing?","Data issue","Stopping test early when p<0.05 inflates false positives","Sample size issue","Metric issue","b","Early stopping based on results increases Type I error.","stats,abtesting"),
(stats_id, ab_testing_id, "medium", "What is novelty effect?","Real improvement","Temporary engagement boost due to new feature","Statistical bias","Sample bias","b","Users engage more with new things temporarily.","stats,abtesting"),
(stats_id, ab_testing_id, "medium", "How to handle novelty effect?","Ignore","Run test longer to let effect stabilize","Stop test early","Reduce sample","b","Longer test duration reveals true long-term effect.","stats,abtesting"),
(stats_id, ab_testing_id, "medium", "What is network effect in A/B testing?","Positive effect","Users in control and treatment influence each other","Sample bias","Data leakage","b","Network effects violate independence assumption.","stats,abtesting"),
(stats_id, ab_testing_id, "medium", "What is Bonferroni correction used for in A/B?","Increase power","Control false positives when testing multiple metrics","Reduce sample size","Increase alpha","b","Multiple metrics need correction to control error rate.","stats,abtesting"),
(stats_id, ab_testing_id, "medium", "What is guardrail metric?","Primary metric","Metric monitored to prevent harm","Conversion metric","Revenue metric","b","Guardrail metrics ensure test doesn't harm key indicators.","stats,abtesting"),
(stats_id, ab_testing_id, "medium", "What is randomization unit?","Sample size","Level at which users are assigned to groups","Metric","Time period","b","Randomization unit is user, session, or page level.","stats,abtesting"),
(stats_id, ab_testing_id, "medium", "User-level vs session-level randomization difference?","Same","User-level more consistent experience","Session better","No difference","b","User-level prevents same user seeing both versions.","stats,abtesting"),
(stats_id, ab_testing_id, "medium", "What is Simpson's paradox?","Data issue","Trend reverses when data is aggregated","Sample bias","Network effect","b","Simpson's paradox: aggregate trends can be misleading.","stats,abtesting"),
(stats_id, ab_testing_id, "medium", "A/B test shows significant result. Next step?","Deploy immediately","Check practical significance and guardrail metrics","Stop all tests","Run more tests","b","Validate business impact before full deployment.","stats,abtesting"),
(stats_id, ab_testing_id, "hard", "A/B test p=0.03 but effect size tiny. What to do?","Deploy","Consider practical significance before deploying","Run more tests","Ignore p-value","b","Statistical significance doesn't guarantee business value.","stats,abtesting"),
(stats_id, ab_testing_id, "hard", "What is sequential testing?","Single analysis","Testing continuously with error control","Batch testing","No testing","b","Sequential testing allows early stopping with controlled error.","stats,abtesting"),
(stats_id, ab_testing_id, "hard", "What is multi-armed bandit?","A/B test variant","Dynamically allocates traffic to better performing variants","Feature selection","Clustering","b","Bandit algorithms optimize while exploring.","stats,abtesting"),
(stats_id, ab_testing_id, "hard", "Difference A/B test vs multi-armed bandit?","Same","A/B explores equally, bandit exploits better variant faster","Bandit more accurate","A/B faster","b","Bandit reduces opportunity cost of testing.","stats,abtesting"),
(stats_id, ab_testing_id, "hard", "What is interaction effect in A/B test?","Main effect","Effect of A varies depending on another variable B","Sample bias","Network effect","b","Interaction means effect differs across subgroups.","stats,abtesting"),
(stats_id, ab_testing_id, "hard", "Checkout button color A/B test shows lift. Is it causal?","Yes always","Only if randomization was proper","No never","Depends on revenue","b","Proper randomization enables causal inference.","stats,abtesting"),
(stats_id, ab_testing_id, "hard", "What is holdout group?","Control group","Group excluded from all experiments as long-term baseline","Treatment group","Random group","b","Holdout measures cumulative experiment impact.","stats,abtesting"),
(stats_id, ab_testing_id, "hard", "How to detect A/A test failure?","P-value check","Significant result in A/A test indicates bias","Sample size","Metric check","b","A/A test should show no significant difference.","stats,abtesting"),
(stats_id, ab_testing_id, "hard", "What is variance reduction technique in A/B?","Increase sample","CUPED uses pre-experiment data to reduce noise","Reduce metrics","Stop early","b","CUPED reduces variance improving test sensitivity.","stats,abtesting"),
(stats_id, ab_testing_id, "hard", "E-commerce: new recommendation algorithm A/B test. Primary metric?","Page views","Revenue per user or conversion rate","Clicks","Bounce rate","b","Revenue per user captures true business impact.","stats,abtesting"),


# ── DATA ANALYSIS: PANDAS ──


(da_id, pandas_da_id, "easy", "What is Pandas primarily used for?","Game development","Data manipulation and analysis","Networking","UI design","b","Pandas is the primary Python library for data analysis.","da,pandas"),
(da_id, pandas_da_id, "easy", "What are two main data structures in Pandas?","Array and List","Series and DataFrame","Tuple and Dict","Stack and Queue","b","Series is 1D and DataFrame is 2D data structure.","da,pandas"),
(da_id, pandas_da_id, "easy", "What is a Series?","2D data","1D labeled array","Dictionary","Matrix","b","Series is a one-dimensional labeled array.","da,pandas"),
(da_id, pandas_da_id, "easy", "What is a DataFrame?","1D array","2D labeled tabular data","Graph","Tree","b","DataFrame is two-dimensional labeled data structure.","da,pandas"),
(da_id, pandas_da_id, "easy", "How to read CSV file in Pandas?","pd.read_csv()","pd.open()","pd.load()","pd.import()","a","pd.read_csv() reads CSV files into DataFrame.","da,pandas"),
(da_id, pandas_da_id, "easy", "What does df.head() return?","Last rows","First 5 rows by default","Middle rows","Random rows","b","head() returns first n rows, default 5.","da,pandas"),
(da_id, pandas_da_id, "easy", "What does df.shape return?","Column names","Tuple of rows and columns","Data types","Index","b","shape returns (rows, columns) tuple.","da,pandas"),
(da_id, pandas_da_id, "easy", "What does df.info() show?","Statistics","Column types, non-null counts, memory","First rows","Last rows","b","info() shows column data types and null counts.","da,pandas"),
(da_id, pandas_da_id, "easy", "What does df.describe() return?","Raw data","Statistical summary of numeric columns","Sorted data","Null values","b","describe() returns count, mean, std, min, max etc.","da,pandas"),
(da_id, pandas_da_id, "easy", "What is loc[] used for?","Position indexing","Label-based indexing","Filtering only","Sorting only","b","loc[] selects rows and columns by label.","da,pandas"),
(da_id, pandas_da_id, "easy", "What is iloc[] used for?","Label indexing","Integer position-based indexing","Filtering","Sorting","b","iloc[] selects by integer position.","da,pandas"),
(da_id, pandas_da_id, "medium", "Difference between loc and iloc?","Same","loc uses labels, iloc uses positions","loc faster","iloc more accurate","b","loc is label-based, iloc is position-based.","da,pandas"),
(da_id, pandas_da_id, "medium", "What does groupby() do?","Sorts data","Groups rows for aggregation operations","Joins tables","Filters rows","b","groupby splits data into groups for aggregation.","da,pandas"),
(da_id, pandas_da_id, "medium", "What does merge() do?","Sort DataFrames","Join two DataFrames like SQL join","Filter data","Group data","b","merge combines DataFrames based on common columns.","da,pandas"),
(da_id, pandas_da_id, "medium", "What does concat() do?","Join on columns","Stack DataFrames vertically or horizontally","Filter data","Group data","b","concat stacks DataFrames along an axis.","da,pandas"),
(da_id, pandas_da_id, "medium", "What does apply() do?","Delete column","Apply function to rows or columns","Sort data","Filter rows","b","apply runs custom function on DataFrame axis.","da,pandas"),
(da_id, pandas_da_id, "medium", "What does pivot_table() do?","Sorts data","Reshapes and aggregates data like Excel pivot","Deletes data","Filters data","b","pivot_table creates summary tables with aggregation.","da,pandas"),
(da_id, pandas_da_id, "medium", "What does melt() do?","Widens data","Unpivots DataFrame from wide to long format","Sorts data","Groups data","b","melt transforms wide data to long format.","da,pandas"),
(da_id, pandas_da_id, "medium", "What is difference between map() and apply()?","Same","map for Series element-wise, apply for row/column","map faster always","apply more accurate","b","map transforms Series, apply works on DataFrame axes.","da,pandas"),
(da_id, pandas_da_id, "medium", "What does value_counts() return?","Unique values only","Frequency count of unique values","Sorted data","Grouped data","a","value_counts returns count of each unique value.","da,pandas"),
(da_id, pandas_da_id, "hard", "Find top 3 customers by revenue using Pandas?","Sort only","groupby customer, sum revenue, sort descending, head(3)","merge only","filter only","b","groupby + sum + sort_values + head solves this.","da,pandas"),
(da_id, pandas_da_id, "hard", "Calculate month-over-month growth in Pandas?","groupby only","groupby month, sum, pct_change()","sort only","merge only","b","pct_change() calculates period-over-period change.","da,pandas"),
(da_id, pandas_da_id, "hard", "Identify churned customers inactive for 30 days?","Sort dates","Filter max purchase date older than 30 days","Merge tables","Group data","b","Filter based on last activity date.","da,pandas"),
(da_id, pandas_da_id, "hard", "What is chunksize parameter in read_csv?","Encoding","Reads file in chunks for memory efficiency","Separator","Header","b","chunksize processes large files in pieces.","da,pandas"),
(da_id, pandas_da_id, "hard", "What does explode() do?","Compress data","Transforms list-like column into separate rows","Sort data","Group data","b","explode unnests list values into separate rows.","da,pandas"),
(da_id, pandas_da_id, "hard", "What is crosstab() used for?","Sorting","Frequency table of two categorical variables","Merging","Filtering","b","crosstab shows frequency distribution of categories.","da,pandas"),
(da_id, pandas_da_id, "hard", "Fastest way to iterate over large DataFrame?","iterrows()","Vectorized operations or apply()","for loop","iteritems()","b","Vectorization is much faster than row iteration.","da,pandas"),
(da_id, pandas_da_id, "hard", "What is query() method?","SQL join","Filter DataFrame using string expression","Sort data","Group data","b","query() filters using readable string conditions.","da,pandas"),
(da_id, pandas_da_id, "hard", "Memory optimization for large DataFrame?","Use more RAM","Use appropriate dtypes and chunking","Delete columns","Sort data","b","Downcasting dtypes significantly reduces memory.","da,pandas"),
(da_id, pandas_da_id, "hard", "Real scenario: merge customer and transaction data, find average order value per segment?","Sort only","merge on customer_id, groupby segment, mean order value","filter only","concat only","b","Merge then groupby aggregation solves this.","da,pandas"),


# ── DATA ANALYSIS: DATA CLEANING ──


(da_id, data_cleaning_id, "easy", "What is data cleaning?","Adding data","Fixing errors, inconsistencies and missing values in data","Sorting data","Visualizing data","b","Data cleaning prepares raw data for analysis.","da,cleaning"),
(da_id, data_cleaning_id, "easy", "What is missing data?","Zero values","Null or NaN values in dataset","Negative values","Duplicate values","b","Missing data appears as NaN or None in Pandas.","da,cleaning"),
(da_id, data_cleaning_id, "easy", "How to detect missing values?","df.head()","df.isnull().sum()","df.describe()","df.info()","b","isnull().sum() counts missing values per column.","da,cleaning"),
(da_id, data_cleaning_id, "easy", "What does dropna() do?","Fill missing values","Remove rows with missing values","Sort data","Group data","b","dropna() removes rows or columns with NaN values.","da,cleaning"),
(da_id, data_cleaning_id, "easy", "What does fillna() do?","Remove nulls","Fill missing values with specified value","Sort data","Group data","b","fillna() replaces NaN with given value.","da,cleaning"),
(da_id, data_cleaning_id, "easy", "Best fill value for numeric missing data?","Zero","Mean or median","Max","Min","b","Mean or median preserves central tendency.","da,cleaning"),
(da_id, data_cleaning_id, "easy", "Best fill value for categorical missing data?","Mean","Mode","Zero","Random","b","Mode is most frequent category for categorical data.","da,cleaning"),
(da_id, data_cleaning_id, "easy", "How to remove duplicate rows?","dropna()","drop_duplicates()","fillna()","groupby()","b","drop_duplicates() removes duplicate rows.","da,cleaning"),
(da_id, data_cleaning_id, "easy", "How to detect duplicates?","isnull()","duplicated()","describe()","info()","b","duplicated() returns boolean mask of duplicate rows.","da,cleaning"),
(da_id, data_cleaning_id, "easy", "How to rename columns?","df.columns = list","df.rename()","Both a and b","df.header()","c","Both direct assignment and rename() work.","da,cleaning"),
(da_id, data_cleaning_id, "medium", "What is outlier?","Normal value","Extreme value far from other data points","Missing value","Duplicate value","b","Outliers are unusual values that may distort analysis.","da,cleaning"),
(da_id, data_cleaning_id, "medium", "How to detect outliers using IQR?","Mean method","Values below Q1-1.5*IQR or above Q3+1.5*IQR","Standard deviation","Z-score only","b","IQR method uses quartile boundaries for outlier detection.","da,cleaning"),
(da_id, data_cleaning_id, "medium", "What is Z-score method for outliers?","IQR method","Values with Z-score > 3 are outliers","Mean method","Median method","b","Z-score > 3 typically indicates outlier.","da,cleaning"),
(da_id, data_cleaning_id, "medium", "How to handle outliers?","Ignore always","Cap, remove, or transform depending on context","Always delete","Always keep","b","Treatment depends on whether outlier is error or valid.","da,cleaning"),
(da_id, data_cleaning_id, "medium", "What is data type mismatch?","Missing data","Column stored as wrong type e.g. numbers as strings","Duplicate data","Outlier","b","Type mismatches prevent proper analysis.","da,cleaning"),
(da_id, data_cleaning_id, "medium", "How to convert column to datetime?","pd.to_string()","pd.to_datetime()","pd.to_numeric()","pd.convert()","b","pd.to_datetime() converts strings to datetime.","da,cleaning"),
(da_id, data_cleaning_id, "medium", "What is data normalization?","Removing nulls","Scaling data to common range","Encoding categories","Removing duplicates","b","Normalization scales values to standard range.","da,cleaning"),
(da_id, data_cleaning_id, "medium", "What is inconsistent data?","Missing values","Same data represented differently in dataset","Outliers","Duplicates","b","Example: Male/male/M all meaning same category.","da,cleaning"),
(da_id, data_cleaning_id, "medium", "How to standardize string columns?","Sort data","str.lower().str.strip()","fillna()","groupby()","b","Lowercase and strip whitespace for consistency.","da,cleaning"),
(da_id, data_cleaning_id, "medium", "What is data imputation?","Removing data","Replacing missing values with estimated values","Sorting data","Encoding data","b","Imputation fills missing values using statistical methods.","da,cleaning"),
(da_id, data_cleaning_id, "hard", "Column has 60% missing values. What to do?","Fill with mean","Consider dropping column or careful imputation","Keep as is","Fill with zero","b","High missingness may indicate column is not useful.","da,cleaning"),
(da_id, data_cleaning_id, "hard", "Transaction data has negative amounts. How to handle?","Delete all","Investigate - may be refunds or errors","Fill with zero","Ignore","b","Negative values need domain understanding first.","da,cleaning"),
(da_id, data_cleaning_id, "hard", "Age column has values like 999. What is this?","Valid age","Sentinel value or data entry error","Outlier to keep","Missing","b","Sentinel values like 999 indicate missing or error.","da,cleaning"),
(da_id, data_cleaning_id, "hard", "What is MCAR in missing data?","Missing completely random","Missing at random","Missing not at random","Missing conditionally","a","MCAR means missingness unrelated to any data.","da,cleaning"),
(da_id, data_cleaning_id, "hard", "What is MAR?","Missing at random - depends on other variables","Missing completely random","Missing not at random","Missing always","a","MAR means missingness depends on observed data.","da,cleaning"),
(da_id, data_cleaning_id, "hard", "What is MNAR?","Missing at random","Missing not at random - depends on missing value itself","MCAR variant","MAR variant","b","MNAR is hardest to handle - value affects its own missingness.","da,cleaning"),
(da_id, data_cleaning_id, "hard", "What is KNN imputation?","Simple mean fill","Fill missing using K nearest neighbor values","Median fill","Mode fill","b","KNN imputation uses similar rows to estimate missing values.","da,cleaning"),
(da_id, data_cleaning_id, "hard", "Real scenario: customer dataset has phone numbers as integers losing leading zeros. Fix?","Sort data","Store as string type","Fill nulls","Group data","b","Phone numbers should be string to preserve leading zeros.","da,cleaning"),
(da_id, data_cleaning_id, "hard", "Date column has mixed formats. Best approach?","Delete column","Use pd.to_datetime with format inference","Fill with mode","Sort data","b","pd.to_datetime handles multiple date formats.","da,cleaning"),
(da_id, data_cleaning_id, "hard", "E-commerce returns dataset - what cleaning steps first?","Model immediately","Check nulls, duplicates, data types, outliers, consistency","Sort data","Plot data","b","Systematic cleaning before any analysis.","da,cleaning"),


# ── DATA ANALYSIS: EDA ──


(da_id, eda_id, "easy", "What is EDA?","Model training","Exploratory Data Analysis - understanding data before modeling","Data cleaning","Feature selection","b","EDA explores data to find patterns, anomalies and insights.","da,eda"),
(da_id, eda_id, "easy", "First step in EDA?","Plot data","Understand data shape, types and basic statistics","Clean data","Build model","b","Start with df.shape, df.info(), df.describe().","da,eda"),
(da_id, eda_id, "easy", "What does df.describe() show?","Raw data","Count, mean, std, min, quartiles, max","Null counts","Column types","b","describe() gives statistical summary of numeric columns.","da,eda"),
(da_id, eda_id, "easy", "What is univariate analysis?","Two variable analysis","Analysis of single variable","Multivariate analysis","Correlation analysis","b","Univariate analysis examines one variable at a time.","da,eda"),
(da_id, eda_id, "easy", "What is bivariate analysis?","Single variable","Analysis of relationship between two variables","Three variables","No variables","b","Bivariate analysis examines relationship between two variables.","da,eda"),
(da_id, eda_id, "easy", "What does correlation show?","Causation","Linear relationship strength between variables","Distribution","Outliers","b","Correlation measures linear relationship between variables.","da,eda"),
(da_id, eda_id, "easy", "Correlation range is?","0 to 1","-1 to 1","0 to infinity","-infinity to infinity","b","Correlation ranges from -1 (negative) to 1 (positive).","da,eda"),
(da_id, eda_id, "easy", "Correlation of 0 means?","Strong relationship","No linear relationship","Perfect relationship","Negative relationship","b","Zero correlation means no linear relationship.","da_eda"),
(da_id, eda_id, "easy", "What chart for distribution of single numeric variable?","Bar chart","Histogram","Pie chart","Line chart","b","Histogram shows distribution of continuous variable.","da,eda"),
(da_id, eda_id, "easy", "What chart for categorical variable frequency?","Histogram","Bar chart","Scatter plot","Box plot","b","Bar chart shows frequency of categories.","da,eda"),
(da_id, eda_id, "medium", "What is a box plot used for?","Distribution only","Showing median, quartiles and outliers","Correlation","Trend analysis","b","Box plot shows five-number summary and outliers.","da,eda"),
(da_id, eda_id, "medium", "What is scatter plot used for?","Frequency","Relationship between two numeric variables","Distribution","Time series","b","Scatter plot reveals relationship between two variables.","da,eda"),
(da_id, eda_id, "medium", "What is a heatmap used for?","Single variable","Visualizing correlation matrix","Time series","Distribution","b","Heatmap shows correlation between multiple variables.","da,eda"),
(da_id, eda_id, "medium", "What is pair plot?","Single variable chart","Scatter plots for all variable pairs","Correlation only","Distribution only","b","Pair plot shows relationships across all variable combinations.","da,eda"),
(da_id, eda_id, "medium", "Difference correlation vs causation?","Same","Correlation is association, causation means one causes other","Causation stronger","No difference","b","Correlation does not imply causation.","da,eda"),
(da_id, eda_id, "medium", "What is multicollinearity?","Missing data","High correlation between independent variables","Outliers","Skewness","b","Multicollinearity causes issues in regression models.","da,eda"),
(da_id, eda_id, "medium", "How to detect multicollinearity?","Box plot","Correlation matrix or VIF","Histogram","Scatter plot","b","VIF > 10 or high correlation indicates multicollinearity.","da,eda"),
(da_id, eda_id, "medium", "What is VIF?","Variance Inflation Factor - measures multicollinearity","Variable Importance Feature","Value In Feature","Variance In Function","a","VIF > 10 indicates problematic multicollinearity.","da,eda"),
(da_id, eda_id, "medium", "What is data profiling?","Model training","Systematic analysis of data quality and characteristics","Feature selection","Data cleaning only","b","Data profiling assesses completeness, accuracy and consistency.","da,eda"),
(da_id, eda_id, "medium", "What is long tail distribution?","Normal distribution","Most values concentrated, few extreme high values","Uniform","Bimodal","b","Long tail common in sales - few products drive most revenue.","da,eda"),
(da_id, eda_id, "hard", "Sales data shows sudden spike. EDA approach?","Ignore","Check if real event, data error, or seasonality","Model immediately","Delete spike","b","Investigate cause before treating as outlier.","da,eda"),
(da_id, eda_id, "hard", "Feature has 95% same value. What to do?","Keep it","Consider dropping - low variance feature","Scale it","Encode it","b","Near-constant features add little information.","da,eda"),
(da_id, eda_id, "hard", "Two features highly correlated. Action?","Keep both","Drop one or use PCA to reduce redundancy","Ignore","Scale both","b","Redundant features waste model capacity.","da,eda"),
(da_id, eda_id, "hard", "What is Yule's Q?","Correlation for numeric","Association measure for binary categorical variables","Regression metric","Distribution test","b","Yule's Q measures association between binary variables.","da,eda"),
(da_id, eda_id, "hard", "What is Spearman correlation?","Linear correlation","Rank-based correlation for non-linear monotonic relationships","Pearson variant","Causal measure","b","Spearman works when relationship is monotonic not linear.","da,eda"),
(da_id, eda_id, "hard", "When to use Spearman over Pearson?","Always","Non-normal data or ordinal variables","Never","Large datasets","b","Spearman is robust to outliers and non-normality.","da,eda"),
(da_id, eda_id, "hard", "What is Simpson's paradox in EDA?","Correlation issue","Aggregate trend reverses when broken into subgroups","Outlier issue","Missing data","b","Always segment data to validate aggregate findings.","da,eda"),
(da_id, eda_id, "hard", "E-commerce EDA: which product category drives most revenue?","Sort data","groupby category, sum revenue, visualize","Clean data","Model data","b","Aggregation and visualization reveals top categories.","da,eda"),
(da_id, eda_id, "hard", "What is cohort analysis?","Single period","Analyzing groups of users who share common characteristic over time","Feature selection","Model evaluation","b","Cohort analysis tracks behavior of user groups over time.","da,eda"),
(da_id, eda_id, "hard", "User retention drops after week 1. EDA next step?","Ignore","Segment users, analyze week 1 behavior, identify drop-off point","Model immediately","Clean data","b","Segmentation reveals which users churn and why.","da,eda"),


# ── DATA ANALYSIS: VISUALIZATION ──


(da_id, visualization_id, "easy", "What is data visualization?","Data cleaning","Visual representation of data to communicate insights","Feature selection","Model training","b","Visualization transforms data into charts and graphs.","da,visualization"),
(da_id, visualization_id, "easy", "Which Python library for basic plotting?","NumPy","Matplotlib","Pandas","Scikit-learn","b","Matplotlib is the foundational Python plotting library.","da,visualization"),
(da_id, visualization_id, "easy", "What is Seaborn used for?","Data cleaning","Statistical data visualization built on Matplotlib","Model training","Feature selection","b","Seaborn makes statistical plots easier with better defaults.","da,visualization"),
(da_id, visualization_id, "easy", "What is Plotly used for?","Static plots","Interactive visualizations","Data cleaning","Model training","b","Plotly creates interactive web-based visualizations.","da,visualization"),
(da_id, visualization_id, "easy", "Best chart for time series data?","Bar chart","Line chart","Pie chart","Histogram","b","Line charts show trends over time clearly.","da,visualization"),
(da_id, visualization_id, "easy", "Best chart for part-to-whole relationship?","Bar chart","Line chart","Pie or donut chart","Scatter plot","c","Pie charts show proportions of a whole.","da,visualization"),
(da_id, visualization_id, "easy", "Best chart for comparing categories?","Scatter plot","Bar chart","Line chart","Histogram","b","Bar charts compare values across categories.","da,visualization"),
(da_id, visualization_id, "easy", "Best chart for relationship between two numeric variables?","Bar chart","Line chart","Scatter plot","Pie chart","c","Scatter plots reveal relationships between two variables.","da,visualization"),
(da_id, visualization_id, "easy", "What does a histogram show?","Categories","Distribution of continuous variable","Two variables","Time series","b","Histogram shows frequency distribution of numeric data.","da,visualization"),
(da_id, visualization_id, "easy", "What does a box plot show?","Single value","Median, quartiles, outliers","Correlation","Time series","b","Box plot summarizes distribution with five-number summary.","da,visualization"),
(da_id, visualization_id, "medium", "What is a violin plot?","Same as box plot","Box plot with distribution shape","Scatter plot","Bar chart","b","Violin plot combines box plot with kernel density estimate.","da,visualization"),
(da_id, visualization_id, "medium", "When to use log scale on axis?","Always","Data spans many orders of magnitude","Never","Small data","b","Log scale handles wide range of values better.","da,visualization"),
(da_id, visualization_id, "medium", "What is a heatmap best used for?","Single variable","Showing correlation matrix or 2D intensity","Time series","Distribution","b","Heatmap visualizes matrix data with color encoding.","da,visualization"),
(da_id, visualization_id, "medium", "What is a treemap?","Line chart variant","Hierarchical data visualization using nested rectangles","Bar chart","Scatter plot","b","Treemap shows part-to-whole for hierarchical data.","da,visualization"),
(da_id, visualization_id, "medium", "What is a waterfall chart?","Line chart","Shows cumulative effect of sequential values","Bar chart","Scatter plot","b","Waterfall charts show how parts contribute to total.","da,visualization"),
(da_id, visualization_id, "medium", "What is a funnel chart used for?","Distribution","Showing drop-off through stages like sales funnel","Correlation","Time series","b","Funnel charts visualize conversion across stages.","da,visualization"),
(da_id, visualization_id, "medium", "What makes a good visualization?","Complex design","Clear message, appropriate chart, minimal clutter","Many colors","3D effects","b","Good viz is simple, accurate and communicates clearly.","da,visualization"),
(da_id, visualization_id, "medium", "What is chart junk?","Good design","Unnecessary visual elements that add no information","Data labels","Axis labels","b","Chart junk clutters without adding insight.","da,visualization"),
(da_id, visualization_id, "medium", "Best color scheme for sequential data?","Random colors","Single hue gradient","Multiple hues","Black and white","b","Sequential palette shows magnitude variation clearly.","da,visualization"),
(da_id, visualization_id, "medium", "Best color scheme for diverging data?","Single hue","Two hue diverging palette from center","Random","Monochrome","b","Diverging palette highlights deviation from midpoint.","da,visualization"),
(da_id, visualization_id, "hard", "Dashboard KPI visualization best practice?","Complex charts","Clear metrics, trend indicators, simple charts","3D effects","Maximum data","b","Dashboards need clarity and quick insight communication.","da,visualization"),
(da_id, visualization_id, "hard", "What is small multiples technique?","Single chart","Same chart repeated for different subgroups","3D chart","Animation","b","Small multiples enable comparison across subgroups.","da,visualization"),
(da_id, visualization_id, "hard", "When to use stacked vs grouped bar chart?","Same always","Stacked for composition, grouped for comparison","Stacked always","Grouped always","b","Stacked shows totals, grouped compares individual values.","da,visualization"),
(da_id, visualization_id, "hard", "What is overplotting?","Too few data points","Too many overlapping data points obscuring pattern","Chart clutter","Wrong chart type","b","Overplotting hides patterns in dense scatter plots.","da,visualization"),
(da_id, visualization_id, "hard", "How to fix overplotting?","Delete data","Use transparency, sampling, or hexbin plots","Add more colors","Use 3D chart","b","Alpha transparency or density plots reveal hidden patterns.","da,visualization"),
(da_id, visualization_id, "hard", "What is Gestalt principle in visualization?","Statistical concept","How humans perceive visual patterns and groupings","Chart type","Color theory","b","Gestalt principles guide effective visual design.","da,visualization"),
(da_id, visualization_id, "hard", "Executive dashboard - which charts?","Complex analytics","Simple KPIs, trend lines, comparison bars","Scatter plots","Histograms","b","Executives need high-level clear summary charts.","da,visualization"),
(da_id, visualization_id, "hard", "What is data ink ratio?","Chart size","Ratio of ink used for data vs total ink","Color ratio","Label ratio","b","Higher data ink ratio means more efficient visualization.","da,visualization"),
(da_id, visualization_id, "hard", "Sales dashboard: show regional performance over time?","Pie chart","Line chart per region or small multiples","Scatter plot","Histogram","b","Line charts show trends, small multiples enable comparison.","da,visualization"),
(da_id, visualization_id, "hard", "What is sparkline?","Full size chart","Tiny inline chart showing trend without axes","Bar chart","Scatter plot","b","Sparklines show trends compactly within tables.","da,visualization"),


# ── DATA ANALYSIS: BUSINESS CASE STUDIES ──


(da_id, business_case_id, "easy", "What is a KPI?","Random metric","Key Performance Indicator measuring business success","Data point","Feature","b","KPIs measure progress toward business objectives.","da,business"),
(da_id, business_case_id, "easy", "What is churn rate?","Growth rate","Percentage of customers who stop using product","Revenue metric","Acquisition rate","b","Churn rate measures customer loss over a period.","da,business"),
(da_id, business_case_id, "easy", "What is customer lifetime value?","Single purchase value","Total revenue expected from customer over relationship","Acquisition cost","Churn rate","b","CLV estimates long-term revenue from a customer.","da,business"),
(da_id, business_case_id, "easy", "What is conversion rate?","Revenue","Percentage completing desired action","Click rate","Bounce rate","b","Conversion rate = conversions / total visitors.","da,business"),
(da_id, business_case_id, "easy", "What is CAC?","Revenue metric","Customer Acquisition Cost","Churn metric","Retention metric","b","CAC is total cost to acquire one new customer.","da,business"),
(da_id, business_case_id, "easy", "Healthy business has CLV vs CAC ratio?","CLV < CAC","CLV > CAC typically 3:1","Equal","Not related","b","CLV should be 3x CAC for healthy unit economics.","da,business"),
(da_id, business_case_id, "easy", "What is MRR?","Monthly Return Rate","Monthly Recurring Revenue","Monthly Retention Rate","Monthly Refund Rate","b","MRR is predictable monthly revenue from subscriptions.","da,business"),
(da_id, business_case_id, "easy", "What is NPS?","Net Profit Score","Net Promoter Score measuring customer loyalty","Net Performance Score","New Product Score","b","NPS measures likelihood of customers recommending product.","da,business"),
(da_id, business_case_id, "easy", "What is DAU/MAU ratio?","Revenue metric","User engagement ratio - daily vs monthly active users","Churn metric","Conversion metric","b","DAU/MAU ratio measures user engagement stickiness.","da,business"),
(da_id, business_case_id, "easy", "What is funnel analysis?","Single metric","Analyzing drop-off at each stage of user journey","Cohort analysis","Churn analysis","b","Funnel analysis identifies where users drop off.","da,business"),
(da_id, business_case_id, "medium", "Revenue dropped 20% this month. First step?","Panic","Break down by segment, product, region to isolate cause","Deploy model","Ignore","b","Segmentation identifies which dimension drove the drop.","da,business"),
(da_id, business_case_id, "medium", "What is cohort analysis?","Single period analysis","Tracking behavior of user groups over time","Feature selection","Model training","b","Cohort analysis reveals retention patterns by group.","da,business"),
(da_id, business_case_id, "medium", "What is retention analysis?","Acquisition analysis","Measuring how many users continue using product over time","Revenue analysis","Conversion analysis","b","Retention measures product stickiness over time.","da,business"),
(da_id, business_case_id, "medium", "What is RFM analysis?","Revenue model","Recency Frequency Monetary customer segmentation","Regression model","Feature method","b","RFM segments customers by purchase behavior.","da,business"),
(da_id, business_case_id, "medium", "What does high recency in RFM mean?","Old customer","Customer purchased recently","Frequent buyer","High spender","b","Recent purchase indicates active engaged customer.","da,business"),
(da_id, business_case_id, "medium", "What is root cause analysis?","Finding revenue","Systematically identifying cause of a problem","Model training","Feature selection","b","RCA traces problem back to its origin.","da,business"),
(da_id, business_case_id, "medium", "What is north star metric?","Any KPI","Single metric capturing core product value","Revenue only","User count only","b","North star metric aligns team toward key value delivery.","da,business"),
(da_id, business_case_id, "medium", "What is data-driven decision making?","Gut feeling","Using data analysis to guide business decisions","Random decisions","Management decisions","b","Data-driven decisions are based on evidence not intuition.","da,business"),
(da_id, business_case_id, "medium", "What is market basket analysis?","Customer segmentation","Finding products frequently purchased together","Churn analysis","Retention analysis","b","Market basket analysis drives recommendation systems.","da,business"),
(da_id, business_case_id, "medium", "What is seasonality in business data?","Random variation","Predictable patterns repeating at regular intervals","Trend","Noise","b","Seasonality causes regular periodic fluctuations.","da,business"),
(da_id, business_case_id, "hard", "User engagement dropped 15% after app update. Analysis approach?","Deploy fix","Compare pre/post metrics, segment users, check specific features","Ignore","Rollback immediately","b","Data analysis identifies which features caused drop.","da,business"),
(da_id, business_case_id, "hard", "Company wants to reduce churn. First analytical step?","Build model immediately","Define churn, measure baseline, identify churned user characteristics","Deploy solution","Collect more data","b","Understanding churn pattern precedes modeling.","da,business"),
(da_id, business_case_id, "hard", "Product team wants new feature. How to prioritize using data?","Gut feeling","Analyze user pain points, usage data, and potential impact","Build immediately","Ignore data","b","Data on user behavior guides feature prioritization.","da,business"),
(da_id, business_case_id, "hard", "What is cannibalization in business analysis?","Growth metric","New product reducing sales of existing product","Churn metric","Retention metric","b","Cannibalization occurs when products compete internally.","da,business"),
(da_id, business_case_id, "hard", "How to measure success of new feature launch?","Revenue only","Define metrics upfront, A/B test, measure against baseline","User feedback only","Ignore data","b","Pre-defined metrics and A/B testing measure feature impact.","da,business"),
(da_id, business_case_id, "hard", "What is contribution margin?","Total revenue","Revenue minus variable costs","Gross profit","Net profit","b","Contribution margin shows profit per unit after variable costs.","da,business"),
(da_id, business_case_id, "hard", "Pricing analysis: which customers are most price sensitive?","Random sample","Analyze elasticity - purchase behavior change with price change","Top customers","All customers","b","Price elasticity analysis identifies sensitive segments.","da,business"),
(da_id, business_case_id, "hard", "What is price elasticity?","Fixed price","Measure of demand change relative to price change","Revenue metric","Cost metric","b","Elasticity > 1 means demand is sensitive to price.","da,business"),
(da_id, business_case_id, "hard", "Operations: delivery time increased, what to analyze?","Ignore","Break down by region, carrier, product type to find bottleneck","Model data","Clean data","b","Segmentation reveals which dimension causes delay.","da,business"),
(da_id, business_case_id, "hard", "Investor asks why Q3 revenue grew but profit fell. Analysis?","Guess","Analyze cost structure - COGS, marketing, operational costs","Ignore","Check revenue only","b","Revenue growth with profit decline signals cost increase.","da,business"),
]

cursor.executemany("""
INSERT INTO questions (
    topic_id, subtopic_id, difficulty,
    question, option_a, option_b, option_c, option_d,
    correct_answer, explanation, tags
) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT DO NOTHING
""", questions)

conn.commit()
conn.close()
print(f"✅ {len(questions)} questions inserted successfully!")