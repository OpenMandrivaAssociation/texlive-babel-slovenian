Name:		texlive-babel-slovenian
Version:	57666
Release:	1
Summary:	Babel support for typesetting Slovenian
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/slovene
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-slovenian.r57666.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-slovenian.doc.r57666.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-slovenian.source.r57666.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the language definition file for support
of Slovenian in babel. Several shortcuts are defined, as well
as translations to Slovenian of standard "LaTeX names".

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-slovenian
%doc %{_texmfdistdir}/doc/generic/babel-slovenian
#- source
%doc %{_texmfdistdir}/source/generic/babel-slovenian

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
