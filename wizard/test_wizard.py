'''
Created on 2020/06/09

@author: iSGMPC
'''
import calendar

from datetime import timedelta
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from email.policy import default
import random
from io import BytesIO
from base64 import decodestring
import base64

import xlsxwriter
from calendar import month_name
from imp import new_module
from lxml.html.builder import HR

 
try:
    import xlwt
    from xlwt import Borders
except ImportError:
    xlwt = None
import logging
_logger = logging.getLogger(__name__)

class test_wizard(models.Model):
    _name = 'test.wizard'
    _description = 'Test Wizard'
    
    #for csv download
    datas = fields.Binary('File')
    
    def get_data_from_test_report(self,data):
        res = []
        test_obj =self.env['test.one'].search([])                  
        res.append({'data':[]})
        for obj_list in test_obj:
            res[0]['data'].append({
                    'name': obj_list.name                  
                })
        return res
     
    @api.model
    def _get_report_values(self,docids,data=None):
        if not data.get('form'):
            raise UserError(_("Form content is missing, this report cannot be printed."))
 
        test_report = self.env['ir.actions.report']._get_report_from_name('sample_project.action_test_report_id')
        return {
            'doc_ids': self.ids,
            'doc_model': test_report.model,
            'get_data_from_test_report': self.get_data_from_test_report(data['form']),
        }
    
    @api.multi
    def print_pdf(self,data):
        print(" print pdf ")
        self.ensure_one()
        [data] = self.read()
       
        test_obj =self.env['test.one'].search([])      
        self.ensure_one()
        self.test_search_result = test_obj.ids
        datas = {
            'ids': [],
            'model': 'test.one',
            'form': data
        }
        return self.env.ref('sample_project.action_test_report_id').report_action(self,data=self._get_report_values(self,data=datas))
        
    @api.multi
    def print_csv(self):
        print("print_csv")
    
    
    
    
    