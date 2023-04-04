{
    'name': 'Action Download',
    'version': '14.0.1.0',
    'summary': 'Added a download file action',
    'description': '''
    Usage：
    ```
    xml:
    <button name="download_file" type="object" string="ObjectButton" class="oe_highlight"/>
    
    python:
    def download_file(self):
        # your_code...
        file_content = b''
        return {
            'type': 'ir.actions.act_download',
            'file_name': 'test.xlsx',  # your file name
            'file_type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', # your file type
            'file_data': base64.encodebytes(file_content), 
        }
        
    ```
    Contact me：624854240@qq.com
    ''',
    'author': 'grey27',
    "license": "LGPL-3",
    'depends': ['web'],
    'data': [
        'views/assets.xml',
    ],
}
