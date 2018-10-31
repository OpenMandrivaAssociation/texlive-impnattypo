Name:		texlive-impnattypo
Version:	1.4
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
%{_texmfdistdir}/tex/latex/impnattypo
%doc %{_texmfdistdir}/doc/latex/impnattypo
#- source
%doc %{_texmfdistdir}/source/latex/impnattypo

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
