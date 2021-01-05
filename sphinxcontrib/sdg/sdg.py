import docutils
from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from jinja2 import Environment, FileSystemLoader
import os

def _get_resource_dir(folder):
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, folder)
    return resource_path

class SDG(Directive):

    option_spec = {
        "file": directives.path,
        "sheet": directives.unchanged,
        "rows": directives.unchanged,
        "selection": directives.unchanged,
        "overflow": directives.unchanged,
        "tablewidth": directives.unchanged,
        "colwidths": directives.unchanged,
        "row_header": directives.unchanged,
        "col_header": directives.unchanged,
    }

    def run(self, icnt=[0]):
        env = self.state.document.settings.env
        document = self.state.document

        icnt[0] += 1

        file_path = self.options.get("file")
        print("FP", file_path)

        if not file_path:
            msg = "file option is missing"
            return [document.reporter.warning(msg, line=self.lineno)]

        #paragraph_node = nodes.paragraph(text="Hello World!")
        #return [paragraph_node]
        loader = FileSystemLoader(_get_resource_dir('templates'))
        _env = Environment(loader=loader,
                           keep_trailing_newline=True,
                           trim_blocks=True,
                           lstrip_blocks=True)

        data = {"content":1234,"register":"abcd","file_name":file_path,"icnt":icnt}
        template = _env.get_template('registers.html')
        html = template.render(**data)
        print('-----------')
        print(html)
        print('-----------')
        return [docutils.nodes.raw('', html, format='html')]



def setup(app):
    app.add_directive("sdg", SDG)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
