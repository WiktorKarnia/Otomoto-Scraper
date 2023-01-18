from scrapy.exporters import CsvItemExporter

class MyCsvItemExporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
        super(MyCsvItemExporter, self).__init__(*args, **kwargs)

    def finish_exporting(self):
        super(MyCsvItemExporter, self).finish_exporting()
        import subprocess
        subprocess.call(["python", "graph.py"])