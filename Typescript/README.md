# 🟦 TypeScript Language Learning Modules

TypeScript is a strongly typed superset of JavaScript that compiles to plain JavaScript. It enables developers to write safer, scalable, and more maintainable applications by adding **static typing**, **advanced type inference**, and **powerful tooling** to the JavaScript ecosystem.

This directory is organized by **language fundamentals**, **type system features**, **object-oriented and functional programming**, and **integration with JavaScript and third-party libraries**.

---

## 🎯 Objectives

- Understand the TypeScript type system and its benefits
- Learn how to write strongly typed, maintainable JavaScript
- Master object-oriented and functional paradigms using TypeScript
- Use generics, interfaces, and advanced types for reusable components
- Configure and use TypeScript effectively in modern development workflows
- Migrate existing JavaScript projects to TypeScript with confidence

---

## 📂 Folder Structure

```bash
TypeScript/
├── paradigm_imperative/             # Basic flow control and logic
│   ├── variables/                   # let, const, type inference
│   ├── operators/                   # Arithmetic, logical, assignment
│   ├── conditionals/                # if, switch, ternary
│   ├── loops/                       # for, while, for...of, etc.
│   ├── functions/                   # Typed parameters, return types
│   └── io_console/                  # Console input/output
├── type_system/                     # Core of TypeScript's static typing
│   ├── primitive_types/             # string, number, boolean, etc.
│   ├── union_and_intersection/      # Combining types
│   ├── type_aliases/                # Custom types with `type`
│   ├── type_assertions/             # Type casting and coercion
│   ├── literal_types/               # Exact value types
│   ├── enums/                       # Enumerated constants
│   └── type_narrowing/              # typeof, instanceof, custom guards
├── object_oriented/                # OOP features in TS
│   ├── classes_and_objects/         # Classes, fields, methods
│   ├── constructors/                # Parameter properties
│   ├── inheritance/                 # `extends` and `super()`
│   ├── access_modifiers/            # public, private, protected
│   ├── abstract_classes/            # Base class blueprints
│   └── interfaces/                   # Structural typing in OOP
├── advanced_types/                 # More powerful type tools
│   ├── generics/                    # Generic types and functions
│   ├── mapped_types/                # keyof, in, etc.
│   ├── conditional_types/           # infer, extends, ternary types
│   ├── utility_types/               # Partial, Pick, Omit, Readonly
│   └── template_literal_types/      # Dynamic string-based types
├── interfaces_and_types/            # Custom contracts
│   ├── interfaces/                  # Interface declarations
│   ├── extending_interfaces/        # Interface composition
│   └── readonly_and_optional/       # Modifiers in interfaces
├── decorators/                      # Experimental metadata annotations
│   ├── class_decorators/            # Applied to class definitions
│   ├── method_decorators/           # Used with class methods
│   └── property_decorators/         # Decorating fields
├── modules_and_namespaces/          # Code organization
│   ├── ESModules/                   # import/export syntax
│   ├── namespaces/                 # Internal modules (legacy)
│   └── declaration_files/           # .d.ts for external JS integration
├── async_programming/               # Handling asynchronous code
│   ├── promises/                    # Promise-based APIs
│   ├── async_await/                 # Modern async style
│   └── fetch_api/                   # Fetch with type-safe responses
├── dom_and_browser/                 # Using TS in frontend apps
│   ├── dom_types/                   # Built-in types for HTML elements
│   ├── event_handling/             # Event listeners with types
│   └── form_handling/              # Validating user input
├── configuration_and_tooling/       # Project setup
│   ├── tsconfig/                    # Compiler options
│   ├── linting_and_formatting/      # ESLint, Prettier integration
│   ├── using_typescript_with_node/  # Backend development
│   └── debugging_ts/                # Source maps and VS Code support
├── migration_and_interoperability/  # Working with JS
│   ├── js_to_ts_migration/          # Converting JS to TS
│   ├── using_js_libraries/          # Installing types via DefinitelyTyped
│   └── hybrid_codebases/            # Mixing JS and TS files
└── testing_and_best_practices/      # Quality and maintainability
    ├── unit_testing/                # Using Jest or Mocha with TS
    ├── typing_tests/                # Asserting type correctness
    └── coding_guidelines/           # Idiomatic and clean code tips
```

---

## 🚀 Tips

- Start with paradigm_imperative/ and type_system/ to understand the fundamentals
- Use interfaces and type aliases to model complex structures early
- Enable strict mode in tsconfig.json to catch bugs proactively
- Practice with real-world examples like form validation and API calls
- Read and experiment with declaration files (\*.d.ts) for third-party packages

<div align="right" style="font-size: 2em;">
    <a href="../README.md">⬅️ Back</a> 
</div>
