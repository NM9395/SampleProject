from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import serialize_exception, content_disposition
import base64
from odoo import registry as registry_get
class Binary(http.Controller):
        
    @http.route('/web/binary/csv_download', type='http', auth="public")
    @serialize_exception
    def csv_download(self,model,id,filename=None, **kw):
        """ Download link for files stored as binary fields.

        :param str model: name of the model to fetch the binary from
        :param str field: binary field
        :param str id: id of the record from which to fetch the binary
        :param str filename: field holding the file's name, if any
        :returns: :class:`werkzeug.wrappers.Response`
        """
        Model = request.env['test.wizard']
        att_model =  Model.browse(int(id))
        filecontent = base64.b64decode(att_model.datas or '')
        if not filecontent:
            return request.not_found()
        else:
            if not filename:
                filename = '%s_%s' % (model.replace('.', '_'), id)
                   
            return request.make_response(filecontent,
                [('Content-Type', 'application/octet-stream'),
                 ('Content-Disposition', content_disposition(filename))])