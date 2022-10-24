#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6646265B586B83CB (mitya57@gmail.com)
#
Name     : pypi-secretstorage
Version  : 3.3.3
Release  : 57
URL      : https://files.pythonhosted.org/packages/53/a4/f48c9d79cb507ed1373477dbceaba7401fd8a23af63b837fa61f1dcd3691/SecretStorage-3.3.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/53/a4/f48c9d79cb507ed1373477dbceaba7401fd8a23af63b837fa61f1dcd3691/SecretStorage-3.3.3.tar.gz
Source1  : https://files.pythonhosted.org/packages/53/a4/f48c9d79cb507ed1373477dbceaba7401fd8a23af63b837fa61f1dcd3691/SecretStorage-3.3.3.tar.gz.asc
Summary  : Python bindings to FreeDesktop.org Secret Service API
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-secretstorage-license = %{version}-%{release}
Requires: pypi-secretstorage-python = %{version}-%{release}
Requires: pypi-secretstorage-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cryptography)
BuildRequires : pypi(jeepney)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
.. image:: https://github.com/mitya57/secretstorage/workflows/tests/badge.svg
:target: https://github.com/mitya57/secretstorage/actions
:alt: GitHub Actions status
.. image:: https://codecov.io/gh/mitya57/secretstorage/branch/master/graph/badge.svg
:target: https://codecov.io/gh/mitya57/secretstorage
:alt: Coverage status
.. image:: https://readthedocs.org/projects/secretstorage/badge/?version=latest
:target: https://secretstorage.readthedocs.io/en/latest/
:alt: ReadTheDocs status

%package license
Summary: license components for the pypi-secretstorage package.
Group: Default

%description license
license components for the pypi-secretstorage package.


%package python
Summary: python components for the pypi-secretstorage package.
Group: Default
Requires: pypi-secretstorage-python3 = %{version}-%{release}

%description python
python components for the pypi-secretstorage package.


%package python3
Summary: python3 components for the pypi-secretstorage package.
Group: Default
Requires: python3-core
Provides: pypi(secretstorage)
Requires: pypi(cryptography)
Requires: pypi(jeepney)

%description python3
python3 components for the pypi-secretstorage package.


%prep
%setup -q -n SecretStorage-3.3.3
cd %{_builddir}/SecretStorage-3.3.3
pushd ..
cp -a SecretStorage-3.3.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1660517868
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-secretstorage
cp %{_builddir}/SecretStorage-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-secretstorage/b23eb98a71ae4e71270872be9d167f785ad043d1
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-secretstorage/b23eb98a71ae4e71270872be9d167f785ad043d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
