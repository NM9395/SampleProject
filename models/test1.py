'''
Created on 2020/05/26

@author: iSGMPC
'''
from odoo import api, fields, models, tools, _
# from adodbapi.examples.xls_write import data
from odoo.exceptions import UserError, ValidationError
import logging

_logger = logging.getLogger(__name__)

class Test1(models.Model):
    _name = 'test.one'
    
    name = fields.Char(string="Name")
    
    age = fields.Integer(string="Age")
    
    test_line = fields.One2many('test.one.line', 'test_line_id', string='Branch Lines' )
    
    test_date = fields.Date() 
    
    test_type = fields.Selection([
                                ("normal", "Normal"),
                                ("country", "Country"),
                                ("love", "Love"),
                                ("horror", "Horror")],required=True)
    
    test_number = fields.Char(string="Number")
    
    test_price = fields.Float(string="Price")
    
    test_validate = fields.Char(string="Validate")
    
    
    
    """ 
        OnChange機能を使って、条件する。
        条件は要件に対して、色々な条件がある。
    """
    @api.onchange('test_type','test_number')
    def onChange_price(self):
        var_type = self.test_type
        #condition
        if var_type == "normal":
            self.test_price = 10.0 
            if self.test_number:
                self.test_price = self.test_price * float(self.test_number)
        elif var_type == "country":
            self.test_price = 20.0
        elif var_type == "love":
            self.test_price = 30.0
        elif var_type == "horror":
            self.test_price = 40.0
            
            
    """
        編集・保存するの場合の機能
    """   
    @api.multi
    def write(self, vals):
        res = super(Test1, self).write(vals)
        if self.test_validate:
            if self.test_validate != "test":
                _logger.warning('Warning Problem is : %s','input data is not test.')
                raise ValidationError(_("Try Again! Please input <test> word."))
        return res 
        
        
    """
        Onchange機能を使って、検証するの場合
    """
    @api.onchange('test_validate')
    def onChange_Validate(self):
        print(" validate ")
#         if self.test_validate:
#             if self.test_validate != "test":
#                 _logger.warning('Warning Problem is : %s','input data is not test.')
#                 raise ValidationError(_("Try Again! Please input <test> word."))
            
            
    """
        バッチ機能
    """   
    @api.multi
    def _run_test_scheduler(self):
        print("-- scheduler function call --")   
            
class Test1_Line(models.Model):
    _name = 'test.one.line'
    
    name = fields.Char(string="Line Name")
    test_line_id = fields.Many2one('test.one', string='Test')
#         

