#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-patron
Version  : 0.4.18
Release  : 7
URL      : https://rubygems.org/downloads/patron-0.4.18.gem
Source0  : https://rubygems.org/downloads/patron-0.4.18.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-patron-lib
BuildRequires : curl-dev
BuildRequires : libidn-dev
BuildRequires : openssl-dev
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-rake-compiler
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-simplecov
BuildRequires : zlib-dev

%description
= Ruby HTTP Client
== SYNOPSIS
Patron is a Ruby HTTP client library based on libcurl. It does not try to expose
the full "power" (read complexity) of libcurl but instead tries to provide a
sane API while taking advantage of libcurl under the hood.

%package lib
Summary: lib components for the rubygem-patron package.
Group: Libraries

%description lib
lib components for the rubygem-patron package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n patron-0.4.18
gem spec %{SOURCE0} -l --ruby > rubygem-patron.gemspec

%build
gem build rubygem-patron.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
patron-0.4.18.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/patron-0.4.18
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/patron-0.4.18.gem
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/patron-0.4.18/gem.build_complete
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/patron-0.4.18/gem_make.out
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/patron-0.4.18/mkmf.log
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/.autotest
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/Gemfile.lock
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/README.txt
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/ext/patron/.RUBYARCHDIR.-.patron.time
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/ext/patron/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/ext/patron/Makefile
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/ext/patron/extconf.rb
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/ext/patron/membuffer.c
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/ext/patron/membuffer.h
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/ext/patron/membuffer.o
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/ext/patron/session_ext.c
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/ext/patron/session_ext.o
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/ext/patron/sglib.h
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/lib/patron.rb
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/lib/patron/error.rb
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/lib/patron/proxy_type.rb
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/lib/patron/request.rb
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/lib/patron/response.rb
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/lib/patron/session.rb
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/lib/patron/util.rb
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/lib/patron/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/patron.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/pic.png
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/script/console
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/script/test_server
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/spec/patron_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/spec/request_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/spec/response_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/spec/session_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/spec/support/test_server.rb
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/spec/util_spec.rb
/usr/lib64/ruby/gems/2.3.0/specifications/patron-0.4.18.gemspec

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/patron-0.4.18/patron/session_ext.so
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/ext/patron/session_ext.so
/usr/lib64/ruby/gems/2.3.0/gems/patron-0.4.18/lib/patron/session_ext.so
