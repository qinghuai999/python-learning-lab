"""
File: DebuggerExercise.py
Author: Shiqi(Kiki) Su
Date: 2025-09-15 15:08
Description: How to use debugger to check issues.
"""

#
# def is_prime(n: int) -> bool:
#     """
#     Return True if 'n' is prime
#     Args:
#         n (int): Input a number
#
#     Returns:
#         bool: True if 'n' is prime. False otherwise.
#     """
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
# def get_prime(n):
#     primes = []
#     i = 2
#     while len(primes) < n:
#         if is_prime(i):
#             primes.append(n)
#         i += 1
#     return primes

def parse_def_line(line: str) -> tuple[str, tuple[str, ...]]:
    """
    Parse a simple Python function signature line (no decorators/indent) such as
    'def foo(a, b=1):' and return (function_name, argument_names_tuple).

    This function is intentionally lightweight: it strips type annotations,
    default values, and star prefixes so that only bare parameter *names*
    are returned. It ignores positional-only markers ("/") and keyword-only
    separators ("*") by design.

    Args:
        line: A single line that starts with 'def ' and ends with a colon.
              Example: 'def foo(a: int, b=1, *args, **kwargs):\\n'

    Returns:
        A tuple (name, args_tuple) where:
            - name is the function name, e.g. 'foo'
            - args_tuple contains only parameter names, e.g. ('a', 'b', 'args', 'kwargs')

    Notes:
        - This does not handle multi-line signatures.
        - Any text after the first closing ')' (e.g., trailing comments) is ignored.
        - Parameter prefixes '*' and '**' are removed from the returned names.
        - For each parameter token, anything after ':' (type) or '=' (default) is discarded.

    Examples:
        >>> parse_def_line("def foo(a: int, b=1, *args, **kwargs):")
        ('foo', ('a', 'b', 'args', 'kwargs'))
    """
    line = line.strip()
    # Reduce the beginning and ending signal
    head = line[len('def '):].rstrip(':\n')
    # Processing the parameters, save only the info inside the parentheses.
    name, _, rest = head.partition('(')
    args_str, _, _ = rest.partition(')')
    # Split parameter part.
    args: list[str] = []
    for raw in args_str.strip(','):
        raw = raw.strip()
        if not raw:
            continue
        # Remove redundant symbol, like '*, = :'
        # Keep names that follow these structural markers.
        if raw == '/' or raw == '*':
            continue
        # Remove leading * or ** from var-positional / var-keyword names
        while raw.startswith('*'):
            raw = raw[1:]
        # Remove type annotation and default assignment
        for sep in (':', '='):
            if sep in raw:
                raw = raw.split(sep, 1)[0].strip()
        if raw:
            args.append(raw)
    return name, tuple(args)


def is_tripquote_line(s: str) -> str | None:
    """
    Check whether the given line begins (ignoring leading spaces) with a
    triple-quote, and return the matched quote token if so, else None.

    Args:
        s (str): A single source line

    Returns:
        "'''" or '""\"' when the line starts with that triple-quote after
        left-stripping; otherwise None.

    """
    s = s.lstrip()
    for q in TRIQUOTES:
        if s.startswith(q):
            return q
    return None

def extract_docstring(lines: list[str],
                      start_idx: int) -> tuple[int, list[str]]:
    """
    Attempt to extract a triple-quoted docstring starting at start_idx.

    If the line at start_idx begins with a triple-quote, we read until
    the matching closing triple-quote (on the same line for single-line
    docstrings or on a later line for multi-line docstrings). We then return:
    (index_of_first_line_after_docstring, docstring_lines_without_quotes)

    If the line at start_idx does not start with a triple-quote, we return:
    (start_idx, [])

    Args:
        lines (list[str]): The entire file split into lines, including newlines.
        start_idx: The index of the line that *may* start with a docstring.

    Returns:
        A pair (end_idx, content_lines) where:
            - end_idx is the index of the line immediately following the
            docstring block (or start_idx if no docstring was found).
            - content_lines is the list of lines inside the docstring with
            both the opening and closing triple-quotes removed; line endings
            are stripped.

    """
    line = lines[start_idx]
    q = is_tripquote_line(line)
    if not q:
        # Not a docstring start
        return  start_idx, []
     # Remove the opening triple-quote from the current line's left-stripped
     # content.
    content = line.lstrip()[len(q):]
    out: list[str] = []

    # Single line docstring closure: opening and closing on the same line
    if q in content:
        anno, _, _ = content.partition(q)
        out.append(anno.rstrip('\n'))
        return start_idx + 1, out

    # Multi-line docstring: collect subsequent lines until closing token
    # Reminder of the first line after opening quotes (maybe empty)
    out.append(content)
    i = start_idx + 1
    while i < len(lines):
        s = lines[i]
        if q in s:
            before, _, _ = s.partition(q)
            out.append(before)
    return i + 1, [x.rstrip('\n') for x in out]


def parse_google_docstring(doc_lines: list[str]
                           ) -> tuple[str, list[str], str, str]:
    """
    Parse a (subset of) google-style docstring into four parts:
        1. summary: First non-empty line
        2. Args: Collected as list[str], one item per non-empty line
        under 'Args'.
        3. Returns: Collected as a single string (lines joined with '\\n')
        4. Preconditions: Collected as a single string (lines joined with
        '\\n')

    Any free-form text *before* the first recognized heading
    (Args:/Returns:/Preconditions:) and *after* the summary is not
    returned here; if you need it as a “details” block, gather it separately
    at call sites.

    Args:
        doc_lines (list[str]): The docstring body split into lines
        (without enclosing quotes).

    Returns:
        (summary, args_list, returns_text, preconditions_text)
        - summary: str (may be empty if doc_lines is empty)
        - args_list: list[str] (each typically 'name (type): description'
        or similar)
        - returns_text: str (joined lines under 'Returns:')
        - preconditions_text: str (joined lines under 'Preconditions:')

    """
    while doc_lines and not doc_lines[0].strip():
        doc_lines.pop(0)



TRIQUOTES = ("'''", "'''")
def find_functions(filename: str) -> str:
    functions = []
    basic_info = ()
    with open(filename, 'r') as file_in:
        lines = file_in.readlines()
    result: list[tuple[int, str, tuple[str, ...]]]
    i = 0
    while i < len(lines):
        raw = lines[i]
        stripped = raw.lstrip()
        if stripped.startswith('def '):
            # row number
            linenum = i + 1
            # name, args =
        i += 1
        for r, line in enumerate(file_in):
            if line.startswith('def '):
                line = line.split('def ', 1)[1]
                name, _, line = line.partition('(')
                args, _, _ = line.partition(')')
                args_list = []
                for arg in args.split(','):
                    args_list.append(arg.strip())
                # result_args = tuple(args_list)
                basic_info = (r, name, args_list)
            content = ''
            if line.startswith('"""'):
                content = line.strip()[3:]
            if line.endswith('"""'):
                content = line.strip()[:-3]
        functions.append([basic_info, content])
    return functions


print(find_functions('FileDict.py'))
