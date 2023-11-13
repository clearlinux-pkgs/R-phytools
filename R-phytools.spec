#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v2
# autospec commit: 250a666
#
Name     : R-phytools
Version  : 2.0.3
Release  : 48
URL      : https://cran.r-project.org/src/contrib/phytools_2.0-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/phytools_2.0-3.tar.gz
Summary  : Phylogenetic Tools for Comparative Biology (and Other Things)
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-ape
Requires: R-clusterGeneration
Requires: R-coda
Requires: R-combinat
Requires: R-doParallel
Requires: R-expm
Requires: R-foreach
Requires: R-maps
Requires: R-mnormt
Requires: R-numDeriv
Requires: R-optimParallel
Requires: R-phangorn
Requires: R-scatterplot3d
BuildRequires : R-ape
BuildRequires : R-clusterGeneration
BuildRequires : R-coda
BuildRequires : R-combinat
BuildRequires : R-doParallel
BuildRequires : R-expm
BuildRequires : R-foreach
BuildRequires : R-maps
BuildRequires : R-mnormt
BuildRequires : R-numDeriv
BuildRequires : R-optimParallel
BuildRequires : R-phangorn
BuildRequires : R-scatterplot3d
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%prep
%setup -q -n phytools
pushd ..
cp -a phytools buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1699901497

%install
export SOURCE_DATE_EPOCH=1699901497
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/phytools/data/bat.tree.rda
/usr/lib64/R/library/phytools/data/bat_virus.data.rda
/usr/lib64/R/library/phytools/data/betaCoV.tree.rda
/usr/lib64/R/library/phytools/data/bonyfish.data.rda
/usr/lib64/R/library/phytools/data/bonyfish.tree.rda
/usr/lib64/R/library/phytools/data/butterfly.data.rda
/usr/lib64/R/library/phytools/data/butterfly.tree.rda
/usr/lib64/R/library/phytools/data/cordylid.data.rda
/usr/lib64/R/library/phytools/data/cordylid.tree.rda
/usr/lib64/R/library/phytools/data/darter.tree.rda
/usr/lib64/R/library/phytools/data/datalist
/usr/lib64/R/library/phytools/data/eel.data.rda
/usr/lib64/R/library/phytools/data/eel.tree.rda
/usr/lib64/R/library/phytools/data/elapidae.tree.rda
/usr/lib64/R/library/phytools/data/flatworm.data.rda
/usr/lib64/R/library/phytools/data/flatworm.tree.rda
/usr/lib64/R/library/phytools/data/liolaemid.data.rda
/usr/lib64/R/library/phytools/data/liolaemid.tree.rda
/usr/lib64/R/library/phytools/data/mammal.data.rda
/usr/lib64/R/library/phytools/data/mammal.geog.rda
/usr/lib64/R/library/phytools/data/mammal.tree.rda
/usr/lib64/R/library/phytools/data/primate.data.rda
/usr/lib64/R/library/phytools/data/primate.tree.rda
/usr/lib64/R/library/phytools/data/salamanders.rda
/usr/lib64/R/library/phytools/data/sunfish.data.rda
/usr/lib64/R/library/phytools/data/sunfish.tree.rda
/usr/lib64/R/library/phytools/data/tortoise.geog.rda
/usr/lib64/R/library/phytools/data/tortoise.tree.rda
/usr/lib64/R/library/phytools/data/tropidurid.data.rda
/usr/lib64/R/library/phytools/data/tropidurid.tree.rda
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
