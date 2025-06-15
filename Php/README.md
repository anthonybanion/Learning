# <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/php/php-original.svg" height="40px" alt="PHP"/> PHP Language Learning Modules

PHP is a general-purpose scripting language especially suited for web development. It supports multiple paradigms, including imperative, procedural, and object-oriented programming. Its syntax is C-style, and it integrates natively with HTML and web servers like Apache and Nginx.

This directory is structured by **programming paradigms**, **core constructs**, and **language-specific capabilities**.

---

## 📂 Folder Structure

```bash
Php/
├── paradigm_imperative/                # Basic imperative constructs in PHP
│   ├── variables/                      # Variable declaration, data types and casting
│   ├── conditionals/                   # if, elseif, else, match statements
│   ├── loops/                          # for, foreach, while, do-while
│   └── input_output/                   # Echo, print, file I/O, and user input
├── paradigm_procedural/                  # Procedural programming concepts in PHP
│   ├── functions/                      # Defining and calling functions
│   ├── variable_scope/                 # Global, local, static variables
│   ├── date_and_time/                  # Working with dates and times
│   ├── modular_code/                   # Splitting code into reusable functions
│   ├── error_handling/                 # try-catch blocks and error handling
│   └── recursion/                      # Writing recursive logic in PHP
├── paradigm_oop/                       # Object-Oriented Programming (OOP) in PHP
│   ├── classes_and_objects/            # Creating classes and object instances
│   ├── inheritance/                    # Parent-child relationships and `extends`
│   ├── encapsulation/                  # Public, private, protected members
│   ├── polymorphism/                   # Interfaces, abstract classes, overriding
│   ├── traits_and_namespaces/          # Code reuse and organization
│   └── magic_methods/                  # `__construct()`, `__toString()`, `__get()`, etc.
├── arrays/                             # Working with arrays in PHP
│   ├── syntax/                         # Indexed, associative, and multidimensional arrays
│   ├── manipulation/                   # Adding, removing, and modifying array elements
│   ├── functions/                      # Built-in functions like `array_push`, `array_pop`
│   ├── search_and_sorting/             # Searching and sorting arrays
│   ├── iteration/                      # Looping through arrays with `foreach`
│   ├── combine_and_merge/              # Merging and combining arrays
│   ├── reduce_and_map/                 # Reducing and mapping arrays
│   ├── filter_and_slice/               # Filtering and slicing arrays
│   ├── keys_and_values/                # Getting keys and values from arrays
│   └── multidimensional/               # Arrays of arrays and table-like data
├── collections/                        # Advanced data structures in PHP
│   ├── collection_classes/             # Overview of PHP's collection classes
│   ├── using_collections/              # How to use collections effectively
│   └── performance_considerations/     # Performance tips for collections
├── strings/                            # String manipulation and pattern matching
│   ├── syntax/                         # String declaration and interpolation
│   ├── functions/                      # Common string functions like `strlen`, `strpos`
│   ├── formatting/                     # Using `.` operator and `sprintf`
│   ├── case_and_whitespace/            # Changing case and trimming whitespace
│   ├── search_and_replace/             # Using `str_replace`, `strpos`, etc.
│   ├── substring/                       # Getting substrings
│   ├── encoding/                       # Handling different encodings (UTF-8, etc.)
│   ├── to_array/                       # Converting strings to arrays and vice versa
│   ├── comparison/                     # Comparing strings with `strcmp`, `strcasecmp`
│   └── escaping/                       # Escaping special characters in strings
├── regular_expressions/                # Pattern matching and manipulation
│   ├── regex_syntax/                   # Basic regex syntax and patterns
│   ├── regex_functions/                # Using `preg_match`, `preg_replace`, etc.
│   ├── capturing_groups/               # Using parentheses for capturing
│   ├── character_classes/              # Using brackets for character sets
│   ├── quantifiers_and_anchors/        # Using `*`, `+`, `?`, and anchors like `^` and `$`
│   ├── lookaheads_and_lookbehinds/     # Advanced assertions in regex
│   ├── escaping_special_characters/    #  Using backslashes to escape characters
│   ├── regex_flags/                    # Modifiers like `i`, `m`, `s`
│   └── performance_tips/               # Optimizing regex performance
├── file/                               # File handling and I/O operations
│   ├── functions/               # Basic file system functions like `file_exists`, `is_dir`
│   ├── reading_writing/                # Reading and writing files with `file_get_contents`, `file_put_contents`
│   ├── streams/                        # Using streams for file operations
│   ├── permissions/                    # Changing file permissions with `chmod`
│   ├── info_and_metadata/              # Getting file info with `stat`, `filetype`
│   ├── uploading/                      # Handling file uploads with `$_FILES`
│   ├── deletion_and_renaming/          # Deleting and renaming files with `unlink`, `rename`
│   ├── directory_operations/           # Creating, deleting, and listing directories
│   ├── error_handling/                 # Handling file errors with `try-catch`
│   └── stream_contexts/                # Using contexts for file streams
├── form_handling/                      # Working with HTML forms in PHP
│   ├── creation/                       # Creating HTML forms with PHP
│   ├── submission/                     # Handling form submissions with `$_POST` and `$_GET`
│   ├── validation/                     # Validating form data before processing
│   ├── uploads/                        # Handling file uploads in forms
│   ├── protection/                     # Implementing Cross-Site Request Forgery protection
│   ├── errors/                         # Displaying and handling form errors
│   ├── security/                       # Securing forms against common vulnerabilities
│   └── helpers/                        # Helper functions for form handling
├── sessions_and_cookies/               # Managing user sessions and cookies
│   ├── session_start_and_destroy/      # Using `session_start()`, `$_SESSION`
│   ├── setting_and_reading_cookies/    # `setcookie()` and `$_COOKIE`
│   └── login_simulation/               # Basic login/logout with sessions
├── scripting_and_cli/                  # PHP as a command-line tool
│   ├── php_cli/                        # Writing CLI scripts with arguments
│   ├── cronjobs/                       # Scheduled PHP scripts via cron
│   └── environment_variables/          # `getenv()` and `.env` handling
├── ecosystem/                          # Exploring the PHP ecosystem
│   ├── composer_and_autoloading/       # Using Composer and PSR-4 autoloading
│   ├── testing_and_linting/            # PHPUnit, PHPStan, and PHP_CodeSniffer
│   └── code_style_and_docblocks/       # PSR standards and doc comments
|── web/                                # PHP in web development
│   ├── server/                         # Setting up Apache or Nginx for PHP
│   ├── apis/                           # Building APIs with PHP
│   ├── request_handling/               # Handling HTTP requests and routing
│   ├── templating_engines/             # Using Twig, Blade, etc.
│   ├── mvc/                            # Model-View-Controller pattern
│   └── restful/                        # Building APIs with PHP
├── databases/                          # Database interaction with PHP
│   ├── mysqli/                         # MySQLi extension for database access
│   ├── PDO/                            # PHP Data Objects for database abstraction
│   ├── ORM_and_Eloquent/               # Object-Relational Mapping with Eloquent
│   └── database_migrations/            # Managing database schema changes
├── security/                           # Securing PHP applications
│   ├── secure_coding/                  # General security practices in PHP
│   ├── error_reporting/                # Configuring error reporting and logging
│   ├── HTTPS_and_SSL/                  # Enforcing HTTPS and SSL/TLS
│   ├── input_sanitization/             # Sanitizing user input to prevent attacks
│   ├── output_encoding/                # Encoding output to prevent XSS
│   ├── session_management/             # Secure session handling
│   ├── password_storage/               # Using `password_hash()` and `password_verify()`
│   ├── file_handling/                  # Secure file handling practices
│   ├── database_access/                # Secure database access practices
│   ├── security_headers/               # Setting security headers in HTTP responses
│   ├── rate_limiting/                  # Preventing abuse with rate limiting
│   ├── input_validation/               # Validating and sanitizing user input
│   ├── SQL_injection/                  # Prepared statements and parameterized queries
│   └── XSS_and_CSRF_protection/        # Cross-Site Scripting and Cross-Site Request Forgery
├── best_practices/                     # Best practices for PHP development
│   ├── coding_standards/               # PSR standards and coding conventions
│   ├── code_organization/              # Structuring PHP projects effectively
│   ├── testing_and_quality_assurance/  # Writing tests and ensuring code quality
│   ├── error_handling_and_logging/     # Best practices for error handling and logging
│   ├── performance_monitoring/         # Tools for monitoring PHP application performance
│   ├── code_refactoring/               # Techniques for improving existing code
│   ├── code_reusability_and_modularity/ # Writing reusable and modular code
│   ├── design_patterns/                # Common design patterns in PHP
│   └── project_structure_and_architecture/ # Structuring PHP projects effectively
└── projects/
    ├── small_projects/                 # Simple projects to practice concepts
    ├── medium_projects/                # Intermediate projects to apply knowledge
    └── large_projects/                 # Complex projects to challenge skills

```

## 🎯 Objectives

- Understand PHP’s imperative and procedural foundations
- Learn full object-oriented programming with PHP
- Handle form submissions, file operations, and input validation
- Explore sessions, cookies, and server-side logic
- Build real-world scripts and command-line tools using PHP
- Get familiar with Composer, testing, and PHP’s broader ecosystem

## 📚 Recommended Resources

- 🔗 PHP Manual (official)
- 🔗 Learn PHP - W3Schools
- 🔗 PHP: The Right Way
- 🔗 PHP Cheat Sheet (DevHints)
- 🔗 PHPUnit — For unit testing

<div align="right" style="font-size: 2em;">
    <a href="../README.md">⬅️ Back</a>
</div>
