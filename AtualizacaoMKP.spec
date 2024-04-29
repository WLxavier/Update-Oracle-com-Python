block_cipher = None

a = Analysis(['att.py'],
             pathex=['C:\\Users\\ti\\Desktop\\Nova pasta'],
             binaries=[],
             datas=[
                ('instantclient_21_9/*', 'instantclient_21_9'),
                ('conect.py', '.'),
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
         cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='AtualizacaoMKP',
          debug=False,
          bootloader_ignore_signals=False,
          icon='C:\\Users\\ti\\Downloads\\icon.ico',
          bootloader_options=None,
          silent=False,
          console=False)

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name='AtualizacaoMKP')