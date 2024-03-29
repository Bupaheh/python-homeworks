import textwrap

_prologue = textwrap.dedent("""\
    \documentclass[12pt]{article}
    
    \\begin{document}
    
    """)

_epilogue = "\n\\end{document}"


def generate_table(table):
    if not isinstance(table, list) or any([not isinstance(row, list) for row in table]):
        raise ValueError('Invalid table')

    cols = len(table[0])

    if any([len(row) != cols for row in table]):
        raise ValueError('Invalid table')

    begin = textwrap.dedent(f"""\
    \\begin{{tabular}}{{{"|c" * cols}|}}
    \\hline
    """)

    body = " \\\\\n\\hline\n".join(" & ".join(map(str, row)) for row in table)

    end = textwrap.dedent(f"""\
         \\\\
        \\hline
        \\end{{tabular}}
        """)

    result = begin + body + end
    return _prologue + result + _epilogue
