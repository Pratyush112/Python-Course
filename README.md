# Python Course for Beginners

Welcome to the **Complete Python Course for Beginners**! This comprehensive course is designed to take you from zero to hero in Python programming.

## Course Structure

This course is organized into modules that progressively build your Python skills:

### Module 1: Foundations
- **[1_dataType.ipynb](1_dataType.ipynb)** - Learn about Python's fundamental data types (int, float, str, bool, list, dict, tuple, set)
- **[2_Variable.py](2_Variable.py)** - Understand how to declare, assign, and manage variables
- **[3_keyworsandIdentifiers.ipynb](3_keyworsandIdentifiers.ipynb)** - Master Python keywords and proper identifier naming conventions
- **[4_userInput.ipynb](4_userInput.ipynb)** - Learn how to interact with users through input/output operations
- **[5_typeConversion.py](5_typeConversion.py)** - Explore type casting and conversion between different data types
- **[6_Literals.py](6_Literals.py)** - Understand literal values and how they are used in Python

### Module 2: Control Flow & Operators
- **[7_Operators.ipynb](7_Operators.ipynb)** - Master all Python operators (Arithmetic, Comparison, Logical, Bitwise, Assignment, Identity, and Membership)
- **[8_IfElse.ipynb](8_IfElse.ipynb)** - Decision making with if, else, elif, and nested conditional statements
- **[9_Loops.ipynb](9_Loops.ipynb)** - Loops (while, for), range function, nested loops, and break/continue/pass

### Module 3: Built-in Functions & Data Structures
- **[10_Builtin_Func_Mod.ipynb](10_Builtin_Func_Mod.ipynb)** - Built-in functions (abs, pow, min/max, round, etc.) and modules (math, random, time)
- **[11_Strings.ipynb](11_Strings.ipynb)** - String indexing, slicing, operations, and string methods (find, replace, format, etc.)
- **[12_Lists.ipynb](12_Lists.ipynb)** - Lists and list operations *(Coming Soon)*
- **[13_sets.ipynb](13_sets.ipynb)** - Sets, set operations (add, difference, intersection, update)
- **[14_dictionary.ipynb](14_dictionary.ipynb)** - Dictionaries and key-value pair operations *(In Progress)*
- **[15_Tuples.ipynb](15_Tuples.ipynb)** - Tuples *(Coming Soon)*

### Module 4: Functions
- **[16_Functions.ipynb](16_Functions.ipynb)** - User-defined functions, default/positional/keyword arguments, *args and **kwargs

### Module 5: Object-Oriented Programming (OOP)
- **[17_OOP_Part1.ipynb](17_OOP_Part1.ipynb)** - Classes, objects, constructors, dunder methods, reference variables, and pass by reference
- **[18_OOP_Part2.ipynb](18_OOP_Part2.ipynb)** - Encapsulation, access modifiers (public/private/protected), static vs instance variables, and collection of objects
- **[19_OOP_Part3.ipynb](19_OOP_Part3.ipynb)** - Inheritance (single, multilevel, hierarchical, multiple, hybrid), method overriding, and super keyword
- **[20_OOP_Part4.ipynb](20_OOP_Part4.ipynb)** - Polymorphism (method overriding, method overloading, operator overloading)

> **More modules are being added regularly!** Stay tuned for additional topics on file handling, exception handling, decorators, and more.

## Learning Outcomes

By the end of this course, you will:
- Understand Python's basic data types and data structures (lists, sets, dictionaries, tuples)
- Work effectively with variables, identifiers, and operators
- Handle user input and output with type conversion
- Control program flow with conditionals and loops
- Use built-in functions and modules (math, random, time)
- Master string manipulation and formatting
- Write reusable code with functions, *args, and **kwargs
- Build custom data types using Object-Oriented Programming
- Apply OOP concepts: Encapsulation, Inheritance, and Polymorphism
- Write clean, readable Python code following best practices

## Getting Started

### Prerequisites
- No prior programming experience needed!
- A text editor or IDE (recommended: VS Code)
- Python 3.x installed on your system

### Installation Guide

#### **Windows**

**Installing Python:**
1. Visit [python.org](https://www.python.org/downloads/)
2. Click the **"Download Python 3.x"** button (latest version)
3. Run the installer executable (.exe)
4. **Important:** Check the box **"Add Python to PATH"** before clicking Install
5. Click **"Install Now"** and wait for completion
6. Verify installation by opening PowerShell/Command Prompt and typing:
   ```bash
   python --version
   ```

**Installing VS Code:**
1. Visit [code.visualstudio.com](https://code.visualstudio.com/)
2. Click **"Download for Windows"**
3. Run the installer and follow the setup wizard
4. After installation, open VS Code
5. Install the Python extension:
   - Go to **Extensions** (Ctrl+Shift+X)
   - Search for "Python"
   - Install the official Python extension by Microsoft

---

#### **macOS**

**Installing Python:**
1. Visit [python.org](https://www.python.org/downloads/macos/)
2. Download the **macOS installer** (latest version)
3. Run the downloaded `.pkg` file and follow the installation wizard
4. Verify installation by opening Terminal and typing:
   ```bash
   python3 --version
   ```
5. Create an alias for convenience (add to ~/.zshrc or ~/.bash_profile):
   ```bash
   alias python=python3
   ```

**Installing VS Code:**
1. Visit [code.visualstudio.com](https://code.visualstudio.com/)
2. Click **"Download for Mac"**
3. Choose between Intel or Apple Silicon version
4. Unzip the downloaded file and drag **Visual Studio Code** to the Applications folder
5. Launch VS Code from Applications
6. Install the Python extension:
   - Go to **Extensions** (Cmd+Shift+X)
   - Search for "Python"
   - Install the official Python extension by Microsoft

---

#### **Linux (Ubuntu/Debian)**

**Installing Python:**
1. Open Terminal and run:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   ```
2. Verify installation:
   ```bash
   python3 --version
   ```
3. Create an alias (add to ~/.bashrc or ~/.zshrc):
   ```bash
   echo "alias python=python3" >> ~/.bashrc
   source ~/.bashrc
   ```

**Installing VS Code:**
1. Download the .deb package from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install using:
   ```bash
   sudo apt install ./code_*.deb
   ```
3. Or install via snap:
   ```bash
   sudo snap install code --classic
   ```
4. Launch VS Code and install the Python extension:
   - Go to **Extensions** (Ctrl+Shift+X)
   - Search for "Python"
   - Install the official Python extension by Microsoft

---

**Linux (Fedora/RHEL/CentOS):**
```bash
sudo dnf install python3 python3-pip python3-venv
```

**Linux (Arch):**
```bash
sudo pacman -S python python-pip
```

### Running the Code

To run any lesson file:

```bash
python filename.py
```

## How to Use This Course

1. Start with **[1_dataType.ipynb](1_dataType.ipynb)** to understand the foundation
2. Progress sequentially through each module
3. Run each notebook/script and experiment with the code
4. Modify examples to deepen your understanding
5. Complete exercises at the end of each module

## Project Setup

This project uses Python 3.x and includes:
- `pyproject.toml` - Project configuration
- `.python-version` - Specifies Python version for the project
- `.gitignore` - Git configuration file

To check your Python version:

```bash
python --version
```

## Tips for Success

- Type out all code examples instead of copying and pasting
- Experiment with changing values and observe the results
- Take notes on key concepts
- Practice regularly and consistently
- Don't rush—understanding is more important than speed

## Next Steps

After completing this course, you'll be ready to explore:
- Exception handling and error management
- File handling and I/O operations
- Decorators and generators
- Regular expressions
- Working with libraries and frameworks (NumPy, Pandas, Flask, Django)
- Database connectivity
- API development

## Support & Share This Course

### ⭐ Star This Repository

Starring helps others discover this course and keeps it visible in the community!

**How to Star on GitHub:**
1. Go to the repository on GitHub
2. Click the **⭐ Star** button in the top-right corner of the page (next to the "Watch" and "Fork" buttons)
3. That's it! You've starred the repository

**Why Star?**
- Helps others find this learning resource
- Shows your appreciation for the course
- Increases visibility in GitHub's trending section
- Keeps you updated with new features and improvements

### Fork This Repository

Forking allows you to create your own copy of the repository where you can make changes, add notes, or create variations of the course.

**How to Fork on GitHub:**
1. Navigate to the repository on GitHub
2. Click the **Fork** button in the top-right corner (it's next to the Star button)
3. Choose where you want to fork it (typically your personal GitHub account)
4. GitHub will create a copy of the entire repository under your account
5. You'll see confirmation that the fork was created successfully

**What You Can Do With a Fork:**
- Add your own notes and comments to the code
- Create additional practice exercises
- Track your progress with custom modifications
- Submit improvements via Pull Requests
- Create variations for learning different Python styles

### After Forking - Clone Your Fork Locally

Once you've forked the repository, clone it to your local machine:

**On Windows (PowerShell):**
```powershell
git clone https://github.com/Pratyush112/Python-Course.git
cd Python
```

**On macOS/Linux (Terminal):**
```bash
git clone https://github.com/Pratyush112/Python-Course.git
cd Python
```

Replace `YOUR-USERNAME` with your actual GitHub username.

### Making Changes to Your Fork

1. Create a new branch for your changes:
   ```bash
   git checkout -b my-changes
   ```

2. Make your edits to the Python files

3. Commit your changes:
   ```bash
   git add .
   git commit -m "Add notes or improvements"
   ```

4. Push to your fork:
   ```bash
   git push origin my-changes
   ```

5. (Optional) Create a Pull Request to contribute back to the original repository

## Contributing

Have suggestions or improvements? Feel free to contribute to this learning resource!

**To Contribute:**
1. Fork the repository (see instructions above)
2. Create a new branch with your improvements
3. Submit a Pull Request with a description of your changes
4. We'll review and merge your contributions!

---

**Happy Learning!** Start with [1_dataType.ipynb](1_dataType.ipynb) today!