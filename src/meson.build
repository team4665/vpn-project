pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'vpn_project')
gnome = import('gnome')

gnome.compile_resources('vpn-project',
  'vpn-project.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'vpn-project.in',
  output: 'vpn-project',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'r-xr--r--'
)

vpn_project_sources = [
  '__init__.py',
  'main.py',
  'window.py',
]

install_data(vpn_project_sources, install_dir: moduledir)
