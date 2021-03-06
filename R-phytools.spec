#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-phytools
Version  : 0.7.80
Release  : 26
URL      : https://cran.r-project.org/src/contrib/phytools_0.7-80.tar.gz
Source0  : https://cran.r-project.org/src/contrib/phytools_0.7-80.tar.gz
Summary  : Phylogenetic Tools for Comparative Biology (and Other Things)
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-ape
Requires: R-clusterGeneration
Requires: R-coda
Requires: R-combinat
Requires: R-expm
Requires: R-maps
Requires: R-mnormt
Requires: R-numDeriv
Requires: R-phangorn
Requires: R-plotrix
Requires: R-scatterplot3d
BuildRequires : R-ape
BuildRequires : R-clusterGeneration
BuildRequires : R-coda
BuildRequires : R-combinat
BuildRequires : R-expm
BuildRequires : R-maps
BuildRequires : R-mnormt
BuildRequires : R-numDeriv
BuildRequires : R-phangorn
BuildRequires : R-plotrix
BuildRequires : R-scatterplot3d
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n phytools
cd %{_builddir}/phytools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622738796

%install
export SOURCE_DATE_EPOCH=1622738796
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library phytools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library phytools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library phytools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc phytools || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/phytools/CITATION
/usr/lib64/R/library/phytools/DESCRIPTION
/usr/lib64/R/library/phytools/INDEX
/usr/lib64/R/library/phytools/Meta/Rd.rds
/usr/lib64/R/library/phytools/Meta/data.rds
/usr/lib64/R/library/phytools/Meta/features.rds
/usr/lib64/R/library/phytools/Meta/hsearch.rds
/usr/lib64/R/library/phytools/Meta/links.rds
/usr/lib64/R/library/phytools/Meta/nsInfo.rds
/usr/lib64/R/library/phytools/Meta/package.rds
/usr/lib64/R/library/phytools/NAMESPACE
/usr/lib64/R/library/phytools/R/phytools
/usr/lib64/R/library/phytools/R/phytools.rdb
/usr/lib64/R/library/phytools/R/phytools.rdx
/usr/lib64/R/library/phytools/data/anole.data.rda
/usr/lib64/R/library/phytools/data/anoletree.rda
/usr/lib64/R/library/phytools/data/datalist
/usr/lib64/R/library/phytools/data/flatworm.data.rda
/usr/lib64/R/library/phytools/data/flatworm.tree.rda
/usr/lib64/R/library/phytools/data/mammal.data.rda
/usr/lib64/R/library/phytools/data/mammal.tree.rda
/usr/lib64/R/library/phytools/data/salamanders.rda
/usr/lib64/R/library/phytools/data/sunfish.data.rda
/usr/lib64/R/library/phytools/data/sunfish.tree.rda
/usr/lib64/R/library/phytools/data/vertebrate.data.rda
/usr/lib64/R/library/phytools/data/vertebrate.tree.rda
/usr/lib64/R/library/phytools/data/wasp.data.rda
/usr/lib64/R/library/phytools/data/wasp.trees.rda
/usr/lib64/R/library/phytools/help/AnIndex
/usr/lib64/R/library/phytools/help/aliases.rds
/usr/lib64/R/library/phytools/help/paths.rds
/usr/lib64/R/library/phytools/help/phytools.rdb
/usr/lib64/R/library/phytools/help/phytools.rdx
/usr/lib64/R/library/phytools/html/00Index.html
/usr/lib64/R/library/phytools/html/R.css
