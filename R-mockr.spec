#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mockr
Version  : 0.1
Release  : 27
URL      : https://cran.r-project.org/src/contrib/mockr_0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mockr_0.1.tar.gz
Summary  : Mocking in R
Group    : Development/Tools
License  : GPL-3.0
Requires: R-lazyeval
BuildRequires : R-lazyeval
BuildRequires : buildreq-R

%description
mockr [![Travis-CI Build Status](https://travis-ci.org/krlmlr/mockr.svg?branch=master)](https://travis-ci.org/krlmlr/mockr) [![Coverage Status](https://img.shields.io/codecov/c/github/krlmlr/mockr/master.svg)](https://codecov.io/github/krlmlr/mockr?branch=master) [![CRAN\_Status\_Badge](http://www.r-pkg.org/badges/version/mockr)](https://cran.r-project.org/package=mockr)
=====================================================================================================================================================================================================================================================================================================================================================================================

%prep
%setup -q -c -n mockr
cd %{_builddir}/mockr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589579870

%install
export SOURCE_DATE_EPOCH=1589579870
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mockr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mockr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mockr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc mockr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mockr/DESCRIPTION
/usr/lib64/R/library/mockr/INDEX
/usr/lib64/R/library/mockr/Meta/Rd.rds
/usr/lib64/R/library/mockr/Meta/features.rds
/usr/lib64/R/library/mockr/Meta/hsearch.rds
/usr/lib64/R/library/mockr/Meta/links.rds
/usr/lib64/R/library/mockr/Meta/nsInfo.rds
/usr/lib64/R/library/mockr/Meta/package.rds
/usr/lib64/R/library/mockr/NAMESPACE
/usr/lib64/R/library/mockr/NEWS.md
/usr/lib64/R/library/mockr/R/mockr
/usr/lib64/R/library/mockr/R/mockr.rdb
/usr/lib64/R/library/mockr/R/mockr.rdx
/usr/lib64/R/library/mockr/help/AnIndex
/usr/lib64/R/library/mockr/help/aliases.rds
/usr/lib64/R/library/mockr/help/mockr.rdb
/usr/lib64/R/library/mockr/help/mockr.rdx
/usr/lib64/R/library/mockr/help/paths.rds
/usr/lib64/R/library/mockr/html/00Index.html
/usr/lib64/R/library/mockr/html/R.css
/usr/lib64/R/library/mockr/tests/testthat.R
/usr/lib64/R/library/mockr/tests/testthat/test-mock.R
