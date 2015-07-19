# revision 30351
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/slovene
# catalog-date 2013-05-08 21:33:39 +0200
# catalog-license lppl1.3
# catalog-version 1.2i
Name:		texlive-babel-slovenian
Version:	1.2i
Release:	9
Summary:	Babel support for typesetting Slovenian
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/slovene
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-slovenian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-slovenian.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-slovenian.source.tar.xz
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
%{_texmfdistdir}/tex/generic/babel-slovenian/slovene.ldf
%doc %{_texmfdistdir}/doc/generic/babel-slovenian/slovene.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-slovenian/slovene.dtx
%doc %{_texmfdistdir}/source/generic/babel-slovenian/slovene.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
