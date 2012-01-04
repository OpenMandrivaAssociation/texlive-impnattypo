# revision 24057
# category Package
# catalog-ctan /macros/latex/contrib/impnattypo
# catalog-date 2011-09-21 17:45:17 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-impnattypo
Version:	1.0
Release:	2
Summary:	Support typography of l'Imprimerie Nationale FranASSaise
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/impnattypo
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/impnattypo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/impnattypo.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/impnattypo.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides useful macros implementing recommendations
by the French Imprimerie Nationale.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/impnattypo/impnattypo.sty
%doc %{_texmfdistdir}/doc/latex/impnattypo/README
%doc %{_texmfdistdir}/doc/latex/impnattypo/impnattypo-fr.pdf
%doc %{_texmfdistdir}/doc/latex/impnattypo/impnattypo.pdf
#- source
%doc %{_texmfdistdir}/source/latex/impnattypo/impnattypo.dtx
%doc %{_texmfdistdir}/source/latex/impnattypo/impnattypo.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
