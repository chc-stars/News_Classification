# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['visualization.py'],
             pathex=['E:\\CODE\\python\\新闻分类\\News_Classification'],
             binaries=[],
             datas=[("E:\CODE\python/新闻分类/News_Classification\data/vocab.txt","vocab"),
             ("E:\CODE\python/新闻分类/News_Classification\Saved_model/","Saved_model")],
             hiddenimports=['PySide2.QtXml'],
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
          [],
          exclude_binaries=True,
          name='visualization',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='visualization')
