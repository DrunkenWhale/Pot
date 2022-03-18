ignore_dir = [".git"]

# copy from "https://github.com/hhatto/gocloc/blob/master/language.go"
lanuage_map = {
    "as": "ActionScript",
    "ada": "Ada",
    "adb": "Ada",
    "ads": "Ada",
    "Ant": "Ant",
    "adoc": "AsciiDoc",
    "asciidoc": "AsciiDoc",
    "asm": "Assembly",
    "S": "Assembly",
    "s": "Assembly",
    "dats": "ATS",
    "sats": "ATS",
    "hats": "ATS",
    "ahk": "AutoHotkey",
    "awk": "Awk",
    "bat": "Batch",
    "btm": "Batch",
    "bb": "BitBake",
    "cbl": "COBOL",
    "cmd": "Batch",
    "bash": "BASH",
    "sh": "Bourne Shell",
    "c": "C",
    "carp": "Carp",
    "csh": "C Shell",
    "ec": "C",
    "erl": "Erlang",
    "hrl": "Erlang",
    "pgc": "C",
    "capnp": "Cap'n Proto",
    "chpl": "Chapel",
    "cs": "C#",
    "clj": "Clojure",
    "coffee": "CoffeeScript",
    "cfm": "ColdFusion",
    "cfc": "ColdFusion CFScript",
    "cmake": "CMake",
    "cc": "C++",
    "cpp": "C++",
    "cxx": "C++",
    "pcc": "C++",
    "c++": "C++",
    "cr": "Crystal",
    "css": "CSS",
    "cu": "CUDA",
    "d": "D",
    "dart": "Dart",
    "dhall": "Dhall",
    "dtrace": "DTrace",
    "dts": "Device Tree",
    "dtsi": "Device Tree",
    "e": "Eiffel",
    "elm": "Elm",
    "el": "LISP",
    "exp": "Expect",
    "ex": "Elixir",
    "exs": "Elixir",
    "feature": "Gherkin",
    "fish": "Fish",
    "fr": "Frege",
    "fst": "F*",
    "F#": "F#",
    "GLSL": "GLSL",
    "vs": "GLSL",
    "shader": "HLSL",
    "cg": "HLSL",
    "cginc": "HLSL",
    "hlsl": "HLSL",
    "lean": "Lean",
    "hlean": "Lean",
    "lgt": "Logtalk",
    "lisp": "LISP",
    "lsp": "LISP",
    "lua": "Lua",
    "ls": "LiveScript",
    "sc": "LISP",
    "f": "FORTRAN Legacy",
    "f77": "FORTRAN Legacy",
    "for": "FORTRAN Legacy",
    "ftn": "FORTRAN Legacy",
    "pfo": "FORTRAN Legacy",
    "f90": "FORTRAN Modern",
    "f95": "FORTRAN Modern",
    "f03": "FORTRAN Modern",
    "f08": "FORTRAN Modern",
    "go": "Go",
    "go2": "Go",
    "groovy": "Groovy",
    "gradle": "Groovy",
    "h": "C Header",
    "hs": "Haskell",
    "hpp": "C++ Header",
    "hh": "C++ Header",
    "html": "HTML",
    "hx": "Haxe",
    "hxx": "C++ Header",
    "idr": "Idris",
    "il": "SKILL",
    "ino": "Arduino Sketch",
    "io": "Io",
    "ipynb": "Jupyter Notebook",
    "jai": "JAI",
    "java": "Java",
    "jsp": "JSP",
    "js": "JavaScript",
    "jl": "Julia",
    "janet": "Janet",
    "json": "JSON",
    "jsx": "JSX",
    "kt": "Kotlin",
    "kts": "Kotlin",
    "lds": "LD Script",
    "less": "LESS",
    "Objective-C": "Objective-C",
    "Matlab": "MATLAB",
    "Mercury": "Mercury",
    "md": "Markdown",
    "markdown": "Markdown",
    "mo": "Motoko",
    "Motoko": "Motoko",
    "nix": "Nix",
    "nsi": "NSIS",
    "nsh": "NSIS",
    "nu": "Nu",
    "ML": "OCaml",
    "ml": "OCaml",
    "mli": "OCaml",
    "mll": "OCaml",
    "mly": "OCaml",
    "mm": "Objective-C++",
    "maven": "Maven",
    "makefile": "Makefile",
    "meson": "Meson",
    "mustache": "Mustache",
    "m4": "M4",
    "l": "lex",
    "nim": "Nim",
    "njk": "Nunjucks",
    "ohm": "Ohm",
    "php": "PHP",
    "pas": "Pascal",
    "PL": "Perl",
    "pl": "Perl",
    "pm": "Perl",
    "plan9sh": "Plan9 Shell",
    "pony": "Pony",
    "ps1": "PowerShell",
    "text": "Plain Text",
    "txt": "Plain Text",
    "polly": "Polly",
    "proto": "Protocol Buffers",
    "py": "Python",
    "pxd": "Cython",
    "pyx": "Cython",
    "q": "Q",
    "qml": "QML",
    "r": "R",
    "R": "R",
    "raml": "RAML",
    "Rebol": "Rebol",
    "red": "Red",
    "rego": "Rego",
    "Rmd": "RMarkdown",
    "rake": "Ruby",
    "rb": "Ruby",
    "resx": "XML resource",
    "ring": "Ring",
    "rkt": "Racket",
    "rhtml": "Ruby HTML",
    "rs": "Rust",
    "rst": "ReStructuredText",
    "sass": "Sass",
    "scala": "Scala",
    "scss": "Sass",
    "scm": "Scheme",
    "sed": "sed",
    "stan": "Stan",
    "sml": "Standard ML",
    "sol": "Solidity",
    "sql": "SQL",
    "svelte": "Svelte",
    "swift": "Swift",
    "t": "Terra",
    "tex": "TeX",
    "thy": "Isabelle",
    "tla": "TLA",
    "sty": "TeX",
    "tcl": "Tcl/Tk",
    "toml": "TOML",
    "TypeScript": "TypeScript",
    "tsx": "TypeScript",
    "tf": "HCL",
    "mat": "Unity-Prefab",
    "prefab": "Unity-Prefab",
    "Coq": "Coq",
    "vala": "Vala",
    "Verilog": "Verilog",
    "csproj": "MSBuild script",
    "vbproj": "MSBuild script",
    "vcproj": "MSBuild script",
    "vb": "Visual Basic",
    "vim": "VimL",
    "vue": "Vue",
    "vy": "Vyper",
    "xml": "XML",
    "XML": "XML",
    "xsd": "XSD",
    "xsl": "XSLT",
    "xslt": "XSLT",
    "wxs": "WiX",
    "yaml": "YAML",
    "yml": "YAML",
    "y": "Yacc",
    "zep": "Zephir",
    "zig": "Zig",
    "zsh": "Zsh",
}