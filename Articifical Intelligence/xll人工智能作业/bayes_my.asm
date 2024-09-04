Rules::Rules(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, long double, long double) [base object constructor]:
        push    rbp
        mov     rbp, rsp
        push    rbx
        sub     rsp, 40
        mov     QWORD PTR [rbp-24], rdi
        mov     QWORD PTR [rbp-32], rsi
        mov     QWORD PTR [rbp-40], rdx
        mov     rax, QWORD PTR [rbp-24]
        mov     rdx, QWORD PTR [rbp-32]
        mov     rsi, rdx
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::basic_string(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) [complete object constructor]
        mov     rax, QWORD PTR [rbp-24]
        lea     rdx, [rax+32]
        mov     rax, QWORD PTR [rbp-40]
        mov     rsi, rax
        mov     rdi, rdx
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::basic_string(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) [complete object constructor]
        mov     rax, QWORD PTR [rbp-24]
        fld     TBYTE PTR [rbp+16]
        fstp    TBYTE PTR [rax+64]
        mov     rax, QWORD PTR [rbp-24]
        fld     TBYTE PTR [rbp+32]
        fstp    TBYTE PTR [rax+80]
        jmp     .L11
        mov     rbx, rax
        mov     rax, QWORD PTR [rbp-24]
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() [complete object destructor]
        mov     rax, rbx
        mov     rdi, rax
        call    _Unwind_Resume
.L11:
        mov     rbx, QWORD PTR [rbp-8]
        leave
        ret
.LC1:
        .string "IF %s THEN (%lf,%lf) %s \n"
Rules::print():
        push    rbp
        mov     rbp, rsp
        push    rbx
        sub     rsp, 56
        mov     QWORD PTR [rbp-24], rdi
        mov     rax, QWORD PTR [rbp-24]
        add     rax, 32
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::c_str() const
        mov     rbx, rax
        mov     rax, QWORD PTR [rbp-24]
        fld     TBYTE PTR [rax+80]
        fstp    TBYTE PTR [rbp-48]
        mov     rax, QWORD PTR [rbp-24]
        fld     TBYTE PTR [rax+64]
        fstp    TBYTE PTR [rbp-64]
        mov     rax, QWORD PTR [rbp-24]
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::c_str() const
        push    QWORD PTR [rbp-40]
        push    QWORD PTR [rbp-48]
        push    QWORD PTR [rbp-56]
        push    QWORD PTR [rbp-64]
        mov     rdx, rbx
        mov     rsi, rax
        mov     edi, OFFSET FLAT:.LC1
        mov     eax, 0
        call    printf
        add     rsp, 32
        nop
        mov     rbx, QWORD PTR [rbp-8]
        leave
        ret
Rules::get_LS_LN():
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        mov     QWORD PTR [rbp-8], rdi
        mov     QWORD PTR [rbp-16], rsi
        mov     rax, QWORD PTR [rbp-16]
        lea     rcx, [rax+64]
        mov     rax, QWORD PTR [rbp-16]
        lea     rdx, [rax+80]
        mov     rax, QWORD PTR [rbp-8]
        mov     rsi, rcx
        mov     rdi, rax
        call    std::pair<long double, long double>::pair<long double&, long double&, true>(long double&, long double&)
        mov     rax, QWORD PTR [rbp-8]
        leave
        ret
Rules::~Rules() [base object destructor]:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        mov     QWORD PTR [rbp-8], rdi
        mov     rax, QWORD PTR [rbp-8]
        add     rax, 32
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() [complete object destructor]
        mov     rax, QWORD PTR [rbp-8]
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() [complete object destructor]
        nop
        leave
        ret
.LC2:
        .string "Input LS1 and LN1 for E1 and H1"
.LC3:
        .string "E1"
.LC4:
        .string "H1"
.LC5:
        .string "Input LS2 and LN2 for E2 and H1"
.LC6:
        .string "E2"
.LC7:
        .string "Input LS3 and LN3 for H1 and H2"
.LC8:
        .string "H2"
.LC9:
        .string "Input LS4 and LN4 for E3 and H2"
.LC10:
        .string "E3"
input_Rules():
        push    rbp
        mov     rbp, rsp
        push    rbx
        sub     rsp, 888
        mov     QWORD PTR [rbp-888], rdi
        mov     rax, QWORD PTR [rbp-888]
        mov     rdi, rax
        call    std::vector<Rules, std::allocator<Rules> >::vector() [complete object constructor]
        mov     esi, OFFSET FLAT:.LC2
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        lea     rax, [rbp-864]
        mov     rsi, rax
        mov     edi, OFFSET FLAT:_ZSt3cin
        call    std::basic_istream<char, std::char_traits<char> >::operator>>(long double&)
        mov     rdx, rax
        lea     rax, [rbp-880]
        mov     rsi, rax
        mov     rdi, rdx
        call    std::basic_istream<char, std::char_traits<char> >::operator>>(long double&)
        lea     rax, [rbp-705]
        mov     QWORD PTR [rbp-24], rax
        nop
        nop
        lea     rdx, [rbp-705]
        lea     rax, [rbp-752]
        mov     esi, OFFSET FLAT:.LC3
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::basic_string<std::allocator<char> >(char const*, std::allocator<char> const&)
        lea     rax, [rbp-657]
        mov     QWORD PTR [rbp-32], rax
        nop
        nop
        lea     rdx, [rbp-657]
        lea     rax, [rbp-704]
        mov     esi, OFFSET FLAT:.LC4
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::basic_string<std::allocator<char> >(char const*, std::allocator<char> const&)
        fld     TBYTE PTR [rbp-864]
        fld     TBYTE PTR [rbp-880]
        lea     rdx, [rbp-704]
        lea     rcx, [rbp-752]
        lea     rax, [rbp-848]
        lea     rsp, [rsp-16]
        fstp    TBYTE PTR [rsp]
        lea     rsp, [rsp-16]
        fstp    TBYTE PTR [rsp]
        mov     rsi, rcx
        mov     rdi, rax
        call    Rules::Rules(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, long double, long double) [complete object constructor]
        add     rsp, 32
        lea     rdx, [rbp-848]
        mov     rax, QWORD PTR [rbp-888]
        mov     rsi, rdx
        mov     rdi, rax
        call    std::vector<Rules, std::allocator<Rules> >::push_back(Rules&&)
        lea     rax, [rbp-848]
        mov     rdi, rax
        call    Rules::~Rules() [complete object destructor]
        lea     rax, [rbp-704]
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() [complete object destructor]
        lea     rax, [rbp-657]
        mov     rdi, rax
        call    std::__new_allocator<char>::~__new_allocator() [base object destructor]
        nop
        lea     rax, [rbp-752]
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() [complete object destructor]
        lea     rax, [rbp-705]
        mov     rdi, rax
        call    std::__new_allocator<char>::~__new_allocator() [base object destructor]
        nop
        mov     rax, QWORD PTR [rbp-888]
        mov     esi, 0
        mov     rdi, rax
        call    std::vector<Rules, std::allocator<Rules> >::operator[](unsigned long)
        mov     rdi, rax
        call    Rules::print()
        mov     esi, OFFSET FLAT:.LC5
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        lea     rax, [rbp-864]
        mov     rsi, rax
        mov     edi, OFFSET FLAT:_ZSt3cin
        call    std::basic_istream<char, std::char_traits<char> >::operator>>(long double&)
        mov     rdx, rax
        lea     rax, [rbp-880]
        mov     rsi, rax
        mov     rdi, rdx
        call    std::basic_istream<char, std::char_traits<char> >::operator>>(long double&)
        lea     rax, [rbp-513]
        mov     QWORD PTR [rbp-40], rax
        nop
        nop
        lea     rdx, [rbp-513]
        lea     rax, [rbp-560]
        mov     esi, OFFSET FLAT:.LC6
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::basic_string<std::allocator<char> >(char const*, std::allocator<char> const&)
        lea     rax, [rbp-465]
        mov     QWORD PTR [rbp-48], rax
        nop
        nop
        lea     rdx, [rbp-465]
        lea     rax, [rbp-512]
        mov     esi, OFFSET FLAT:.LC4
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::basic_string<std::allocator<char> >(char const*, std::allocator<char> const&)
        fld     TBYTE PTR [rbp-864]
        fld     TBYTE PTR [rbp-880]
        lea     rdx, [rbp-512]
        lea     rcx, [rbp-560]
        lea     rax, [rbp-656]
        lea     rsp, [rsp-16]
        fstp    TBYTE PTR [rsp]
        lea     rsp, [rsp-16]
        fstp    TBYTE PTR [rsp]
        mov     rsi, rcx
        mov     rdi, rax
        call    Rules::Rules(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, long double, long double) [complete object constructor]
        add     rsp, 32
        lea     rdx, [rbp-656]
        mov     rax, QWORD PTR [rbp-888]
        mov     rsi, rdx
        mov     rdi, rax
        call    std::vector<Rules, std::allocator<Rules> >::push_back(Rules&&)
        lea     rax, [rbp-656]
        mov     rdi, rax
        call    Rules::~Rules() [complete object destructor]
        lea     rax, [rbp-512]
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() [complete object destructor]
        lea     rax, [rbp-465]
        mov     rdi, rax
        call    std::__new_allocator<char>::~__new_allocator() [base object destructor]
        nop
        lea     rax, [rbp-560]
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() [complete object destructor]
        lea     rax, [rbp-513]
        mov     rdi, rax
        call    std::__new_allocator<char>::~__new_allocator() [base object destructor]
        nop
        mov     rax, QWORD PTR [rbp-888]
        mov     esi, 1
        mov     rdi, rax
        call    std::vector<Rules, std::allocator<Rules> >::operator[](unsigned long)
        mov     rdi, rax
        call    Rules::print()
        mov     esi, OFFSET FLAT:.LC7
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        lea     rax, [rbp-864]
        mov     rsi, rax
        mov     edi, OFFSET FLAT:_ZSt3cin
        call    std::basic_istream<char, std::char_traits<char> >::operator>>(long double&)
        mov     rdx, rax
        lea     rax, [rbp-880]
        mov     rsi, rax
        mov     rdi, rdx
        call    std::basic_istream<char, std::char_traits<char> >::operator>>(long double&)
        lea     rax, [rbp-321]
        mov     QWORD PTR [rbp-56], rax
        nop
        nop
        lea     rdx, [rbp-321]
        lea     rax, [rbp-368]
        mov     esi, OFFSET FLAT:.LC4
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::basic_string<std::allocator<char> >(char const*, std::allocator<char> const&)
        lea     rax, [rbp-273]
        mov     QWORD PTR [rbp-64], rax
        nop
        nop
        lea     rdx, [rbp-273]
        lea     rax, [rbp-320]
        mov     esi, OFFSET FLAT:.LC8
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::basic_string<std::allocator<char> >(char const*, std::allocator<char> const&)
        fld     TBYTE PTR [rbp-864]
        fld     TBYTE PTR [rbp-880]
        lea     rdx, [rbp-320]
        lea     rcx, [rbp-368]
        lea     rax, [rbp-464]
        lea     rsp, [rsp-16]
        fstp    TBYTE PTR [rsp]
        lea     rsp, [rsp-16]
        fstp    TBYTE PTR [rsp]
        mov     rsi, rcx
        mov     rdi, rax
        call    Rules::Rules(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, long double, long double) [complete object constructor]
        add     rsp, 32
        lea     rdx, [rbp-464]
        mov     rax, QWORD PTR [rbp-888]
        mov     rsi, rdx
        mov     rdi, rax
        call    std::vector<Rules, std::allocator<Rules> >::push_back(Rules&&)
        lea     rax, [rbp-464]
        mov     rdi, rax
        call    Rules::~Rules() [complete object destructor]
        lea     rax, [rbp-320]
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() [complete object destructor]
        lea     rax, [rbp-273]
        mov     rdi, rax
        call    std::__new_allocator<char>::~__new_allocator() [base object destructor]
        nop
        lea     rax, [rbp-368]
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() [complete object destructor]
        lea     rax, [rbp-321]
        mov     rdi, rax
        call    std::__new_allocator<char>::~__new_allocator() [base object destructor]
        nop
        mov     rax, QWORD PTR [rbp-888]
        mov     esi, 2
        mov     rdi, rax
        call    std::vector<Rules, std::allocator<Rules> >::operator[](unsigned long)
        mov     rdi, rax
        call    Rules::print()
        mov     esi, OFFSET FLAT:.LC9
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        lea     rax, [rbp-864]
        mov     rsi, rax
        mov     edi, OFFSET FLAT:_ZSt3cin
        call    std::basic_istream<char, std::char_traits<char> >::operator>>(long double&)
        mov     rdx, rax
        lea     rax, [rbp-880]
        mov     rsi, rax
        mov     rdi, rdx
        call    std::basic_istream<char, std::char_traits<char> >::operator>>(long double&)
        lea     rax, [rbp-129]
        mov     QWORD PTR [rbp-72], rax
        nop
        nop
        lea     rdx, [rbp-129]
        lea     rax, [rbp-176]
        mov     esi, OFFSET FLAT:.LC10
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::basic_string<std::allocator<char> >(char const*, std::allocator<char> const&)
        lea     rax, [rbp-81]
        mov     QWORD PTR [rbp-80], rax
        nop
        nop
        lea     rdx, [rbp-81]
        lea     rax, [rbp-128]
        mov     esi, OFFSET FLAT:.LC8
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::basic_string<std::allocator<char> >(char const*, std::allocator<char> const&)
        fld     TBYTE PTR [rbp-864]
        fld     TBYTE PTR [rbp-880]
        lea     rdx, [rbp-128]
        lea     rcx, [rbp-176]
        lea     rax, [rbp-272]
        lea     rsp, [rsp-16]
        fstp    TBYTE PTR [rsp]
        lea     rsp, [rsp-16]
        fstp    TBYTE PTR [rsp]
        mov     rsi, rcx
        mov     rdi, rax
        call    Rules::Rules(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, long double, long double) [complete object constructor]
        add     rsp, 32
        lea     rdx, [rbp-272]
        mov     rax, QWORD PTR [rbp-888]
        mov     rsi, rdx
        mov     rdi, rax
        call    std::vector<Rules, std::allocator<Rules> >::push_back(Rules&&)
        lea     rax, [rbp-272]
        mov     rdi, rax
        call    Rules::~Rules() [complete object destructor]
        lea     rax, [rbp-128]
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() [complete object destructor]
        lea     rax, [rbp-81]
        mov     rdi, rax
        call    std::__new_allocator<char>::~__new_allocator() [base object destructor]
        nop
        lea     rax, [rbp-176]
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() [complete object destructor]
        lea     rax, [rbp-129]
        mov     rdi, rax
        call    std::__new_allocator<char>::~__new_allocator() [base object destructor]
        nop
        mov     rax, QWORD PTR [rbp-888]
        mov     esi, 3
        mov     rdi, rax
        call    std::vector<Rules, std::allocator<Rules> >::operator[](unsigned long)
        mov     rdi, rax
        call    Rules::print()
        jmp     .L55
        mov     rbx, rax
        lea     rax, [rbp-848]
        mov     rdi, rax
        call    Rules::~Rules() [complete object destructor]
        jmp     .L22
        mov     rbx, rax
.L22:
        lea     rax, [rbp-704]
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() [complete object destructor]
        jmp     .L23
        mov     rbx, rax
.L23:
        lea     rax, [rbp-657]
        mov     rdi, rax
        call    std::__new_allocator<char>::~__new_allocator() [base object destructor]
        nop
        lea     rax, [rbp-752]
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() [complete object destructor]
        jmp     .L24
        mov     rbx, rax
.L24:
        lea     rax, [rbp-705]
        mov     rdi, rax
        call    std::__new_allocator<char>::~__new_allocator() [base object destructor]
        nop
        jmp     .L25
        mov     rbx, rax
        lea     rax, [rbp-656]
        mov     rdi, rax
        call    Rules::~Rules() [complete object destructor]
        jmp     .L27
        mov     rbx, rax
.L27:
        lea     rax, [rbp-512]
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() [complete object destructor]
        jmp     .L28
        mov     rbx, rax
.L28:
        lea     rax, [rbp-465]
        mov     rdi, rax
        call    std::__new_allocator<char>::~__new_allocator() [base object destructor]
        nop
        lea     rax, [rbp-560]
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() [complete object destructor]
        jmp     .L29
        mov     rbx, rax
.L29:
        lea     rax, [rbp-513]
        mov     rdi, rax
        call    std::__new_allocator<char>::~__new_allocator() [base object destructor]
        nop
        jmp     .L25
        mov     rbx, rax
        lea     rax, [rbp-464]
        mov     rdi, rax
        call    Rules::~Rules() [complete object destructor]
        jmp     .L31
        mov     rbx, rax
.L31:
        lea     rax, [rbp-320]
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() [complete object destructor]
        jmp     .L32
        mov     rbx, rax
.L32:
        lea     rax, [rbp-273]
        mov     rdi, rax
        call    std::__new_allocator<char>::~__new_allocator() [base object destructor]
        nop
        lea     rax, [rbp-368]
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() [complete object destructor]
        jmp     .L33
        mov     rbx, rax
.L33:
        lea     rax, [rbp-321]
        mov     rdi, rax
        call    std::__new_allocator<char>::~__new_allocator() [base object destructor]
        nop
        jmp     .L25
        mov     rbx, rax
        lea     rax, [rbp-272]
        mov     rdi, rax
        call    Rules::~Rules() [complete object destructor]
        jmp     .L35
        mov     rbx, rax
.L35:
        lea     rax, [rbp-128]
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() [complete object destructor]
        jmp     .L36
        mov     rbx, rax
.L36:
        lea     rax, [rbp-81]
        mov     rdi, rax
        call    std::__new_allocator<char>::~__new_allocator() [base object destructor]
        nop
        lea     rax, [rbp-176]
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() [complete object destructor]
        jmp     .L37
        mov     rbx, rax
.L37:
        lea     rax, [rbp-129]
        mov     rdi, rax
        call    std::__new_allocator<char>::~__new_allocator() [base object destructor]
        nop
        jmp     .L25
        mov     rbx, rax
.L25:
        mov     rax, QWORD PTR [rbp-888]
        mov     rdi, rax
        call    std::vector<Rules, std::allocator<Rules> >::~vector() [complete object destructor]
        mov     rax, rbx
        mov     rdi, rax
        call    _Unwind_Resume
.L55:
        mov     rax, QWORD PTR [rbp-888]
        mov     rbx, QWORD PTR [rbp-8]
        leave
        ret
.LC11:
        .string "Now input O(H1)"
.LC12:
        .string "Now input O(H2)"
input_OH():
        push    rbp
        mov     rbp, rsp
        push    rbx
        sub     rsp, 40
        mov     QWORD PTR [rbp-40], rdi
        mov     rax, QWORD PTR [rbp-40]
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::vector() [complete object constructor]
        mov     esi, OFFSET FLAT:.LC11
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        lea     rax, [rbp-32]
        mov     rsi, rax
        mov     edi, OFFSET FLAT:_ZSt3cin
        call    std::basic_istream<char, std::char_traits<char> >::operator>>(long double&)
        lea     rdx, [rbp-32]
        mov     rax, QWORD PTR [rbp-40]
        mov     rsi, rdx
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::push_back(long double const&)
        mov     esi, OFFSET FLAT:.LC12
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        lea     rax, [rbp-32]
        mov     rsi, rax
        mov     edi, OFFSET FLAT:_ZSt3cin
        call    std::basic_istream<char, std::char_traits<char> >::operator>>(long double&)
        lea     rdx, [rbp-32]
        mov     rax, QWORD PTR [rbp-40]
        mov     rsi, rdx
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::push_back(long double const&)
        jmp     .L63
        mov     rbx, rax
        mov     rax, QWORD PTR [rbp-40]
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::~vector() [complete object destructor]
        mov     rax, rbx
        mov     rdi, rax
        call    _Unwind_Resume
.L63:
        mov     rax, QWORD PTR [rbp-40]
        mov     rbx, QWORD PTR [rbp-8]
        leave
        ret
.LC13:
        .string "Now input C(E%d|S%d)\n"
input_C_ES():
        push    rbp
        mov     rbp, rsp
        push    rbx
        sub     rsp, 56
        mov     QWORD PTR [rbp-56], rdi
        mov     rax, QWORD PTR [rbp-56]
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::vector() [complete object constructor]
        mov     DWORD PTR [rbp-20], 1
        jmp     .L65
.L66:
        mov     edx, DWORD PTR [rbp-20]
        mov     eax, DWORD PTR [rbp-20]
        mov     esi, eax
        mov     edi, OFFSET FLAT:.LC13
        mov     eax, 0
        call    printf
        lea     rax, [rbp-48]
        mov     rsi, rax
        mov     edi, OFFSET FLAT:_ZSt3cin
        call    std::basic_istream<char, std::char_traits<char> >::operator>>(long double&)
        lea     rdx, [rbp-48]
        mov     rax, QWORD PTR [rbp-56]
        mov     rsi, rdx
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::push_back(long double const&)
        add     DWORD PTR [rbp-20], 1
.L65:
        cmp     DWORD PTR [rbp-20], 3
        jle     .L66
        jmp     .L70
        mov     rbx, rax
        mov     rax, QWORD PTR [rbp-56]
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::~vector() [complete object destructor]
        mov     rax, rbx
        mov     rdi, rax
        call    _Unwind_Resume
.L70:
        mov     rax, QWORD PTR [rbp-56]
        mov     rbx, QWORD PTR [rbp-8]
        leave
        ret
My_Bayes::My_Bayes() [base object constructor]:
        push    rbp
        mov     rbp, rsp
        push    rbx
        sub     rsp, 120
        mov     QWORD PTR [rbp-120], rdi
        mov     rax, QWORD PTR [rbp-120]
        mov     rdi, rax
        call    std::vector<Rules, std::allocator<Rules> >::vector() [complete object constructor]
        mov     rax, QWORD PTR [rbp-120]
        add     rax, 24
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::vector() [complete object constructor]
        mov     rax, QWORD PTR [rbp-120]
        add     rax, 48
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::vector() [complete object constructor]
        lea     rax, [rbp-112]
        mov     rdi, rax
        call    input_Rules()
        mov     rax, QWORD PTR [rbp-120]
        lea     rdx, [rbp-112]
        mov     rsi, rdx
        mov     rdi, rax
        call    std::vector<Rules, std::allocator<Rules> >::operator=(std::vector<Rules, std::allocator<Rules> >&&)
        lea     rax, [rbp-112]
        mov     rdi, rax
        call    std::vector<Rules, std::allocator<Rules> >::~vector() [complete object destructor]
        lea     rax, [rbp-80]
        mov     rdi, rax
        call    input_OH()
        mov     rax, QWORD PTR [rbp-120]
        lea     rdx, [rax+24]
        lea     rax, [rbp-80]
        mov     rsi, rax
        mov     rdi, rdx
        call    std::vector<long double, std::allocator<long double> >::operator=(std::vector<long double, std::allocator<long double> >&&)
        lea     rax, [rbp-80]
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::~vector() [complete object destructor]
        lea     rax, [rbp-48]
        mov     rdi, rax
        call    input_C_ES()
        mov     rax, QWORD PTR [rbp-120]
        lea     rdx, [rax+48]
        lea     rax, [rbp-48]
        mov     rsi, rax
        mov     rdi, rdx
        call    std::vector<long double, std::allocator<long double> >::operator=(std::vector<long double, std::allocator<long double> >&&)
        lea     rax, [rbp-48]
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::~vector() [complete object destructor]
        jmp     .L74
        mov     rbx, rax
        mov     rax, QWORD PTR [rbp-120]
        add     rax, 48
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::~vector() [complete object destructor]
        mov     rax, QWORD PTR [rbp-120]
        add     rax, 24
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::~vector() [complete object destructor]
        mov     rax, QWORD PTR [rbp-120]
        mov     rdi, rax
        call    std::vector<Rules, std::allocator<Rules> >::~vector() [complete object destructor]
        mov     rax, rbx
        mov     rdi, rax
        call    _Unwind_Resume
.L74:
        mov     rbx, QWORD PTR [rbp-8]
        leave
        ret
My_Bayes::From_O_get_P(long double):
        push    rbp
        mov     rbp, rsp
        mov     QWORD PTR [rbp-8], rdi
        fld     TBYTE PTR [rbp+16]
        fld1
        faddp   st(1), st
        fld     TBYTE PTR [rbp+16]
        fdivrp  st(1), st
        pop     rbp
        ret
My_Bayes::From_P_get_O(long double):
        push    rbp
        mov     rbp, rsp
        mov     QWORD PTR [rbp-8], rdi
        fld1
        fld     TBYTE PTR [rbp+16]
        fsubp   st(1), st
        fld     TBYTE PTR [rbp+16]
        fdivrp  st(1), st
        pop     rbp
        ret
My_Bayes::Updated_Bayes_O_HE_O_H_Not_E(std::pair<long double, long double>, long double):
        push    rbp
        mov     rbp, rsp
        sub     rsp, 48
        mov     QWORD PTR [rbp-40], rdi
        mov     QWORD PTR [rbp-48], rsi
        fld     TBYTE PTR [rbp+16]
        fld     TBYTE PTR [rbp+48]
        fmulp   st(1), st
        fstp    TBYTE PTR [rbp-16]
        fld     TBYTE PTR [rbp+32]
        fld     TBYTE PTR [rbp+48]
        fmulp   st(1), st
        fstp    TBYTE PTR [rbp-32]
        lea     rdx, [rbp-32]
        lea     rcx, [rbp-16]
        mov     rax, QWORD PTR [rbp-40]
        mov     rsi, rcx
        mov     rdi, rax
        call    std::pair<long double, long double>::pair<long double&, long double&, true>(long double&, long double&)
        mov     rax, QWORD PTR [rbp-40]
        leave
        ret
.LC16:
        .string "ERROR P(E|S)"
My_Bayes::get_P_HS_from_EH_Linear_Interpolation(long double, long double, long double, long double, long double):
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        mov     QWORD PTR [rbp-8], rdi
        fldz
        fld     TBYTE PTR [rbp+48]
        fcomip  st, st(1)
        fstp    st(0)
        jb      .L82
        fld     TBYTE PTR [rbp+48]
        fld     TBYTE PTR [rbp+32]
        fcomip  st, st(1)
        fstp    st(0)
        jbe     .L82
        fld     TBYTE PTR [rbp+16]
        fld     TBYTE PTR [rbp+80]
        fsubp   st(1), st
        fld     TBYTE PTR [rbp+32]
        fdivp   st(1), st
        fld     TBYTE PTR [rbp+48]
        fmulp   st(1), st
        fld     TBYTE PTR [rbp+80]
        faddp   st(1), st
        jmp     .L85
.L82:
        fld     TBYTE PTR [rbp+32]
        fld     TBYTE PTR [rbp+48]
        fcomip  st, st(1)
        fstp    st(0)
        jb      .L86
        fld     TBYTE PTR [rbp+48]
        fld1
        fcomip  st, st(1)
        fstp    st(0)
        jb      .L86
        fld     TBYTE PTR [rbp+64]
        fld     TBYTE PTR [rbp+16]
        fsubp   st(1), st
        fld1
        fld     TBYTE PTR [rbp+32]
        fsubp   st(1), st
        fdivp   st(1), st
        fld     TBYTE PTR [rbp+48]
        fld     TBYTE PTR [rbp+32]
        fsubp   st(1), st
        fmulp   st(1), st
        fld     TBYTE PTR [rbp+16]
        faddp   st(1), st
        jmp     .L85
.L86:
        mov     esi, OFFSET FLAT:.LC16
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        mov     edi, 0
        call    exit
.L85:
        leave
        ret
My_Bayes::get_P_HS_From_CP_formula(long double, long double, long double, long double):
        push    rbp
        mov     rbp, rsp
        mov     QWORD PTR [rbp-8], rdi
        fld     TBYTE PTR [rbp+64]
        fldz
        fcomip  st, st(1)
        fstp    st(0)
        jb      .L98
        fld     TBYTE PTR [rbp+16]
        fld     TBYTE PTR [rbp+48]
        fsubp   st(1), st
        fld     TBYTE PTR [rbp+64]
        fld     TBYTE PTR .LC17[rip]
        fmulp   st(1), st
        fld1
        faddp   st(1), st
        fmulp   st(1), st
        fld     TBYTE PTR [rbp+48]
        faddp   st(1), st
        jmp     .L96
.L98:
        fld     TBYTE PTR [rbp+32]
        fld     TBYTE PTR [rbp+16]
        fsubp   st(1), st
        fld     TBYTE PTR .LC17[rip]
        fmulp   st(1), st
        fld     TBYTE PTR [rbp+64]
        fmulp   st(1), st
        fld     TBYTE PTR [rbp+16]
        faddp   st(1), st
.L96:
        pop     rbp
        ret
My_Bayes::Get_Posterior_Probability_From_All_Observation(std::vector<long double, std::allocator<long double> >, long double):
        push    rbp
        mov     rbp, rsp
        sub     rsp, 80
        mov     QWORD PTR [rbp-72], rdi
        mov     QWORD PTR [rbp-80], rsi
        fld1
        fstp    TBYTE PTR [rbp-16]
        mov     rax, QWORD PTR [rbp-80]
        mov     QWORD PTR [rbp-24], rax
        mov     rax, QWORD PTR [rbp-24]
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::begin()
        mov     QWORD PTR [rbp-56], rax
        mov     rax, QWORD PTR [rbp-24]
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::end()
        mov     QWORD PTR [rbp-64], rax
        jmp     .L100
.L101:
        lea     rax, [rbp-56]
        mov     rdi, rax
        call    __gnu_cxx::__normal_iterator<long double*, std::vector<long double, std::allocator<long double> > >::operator*() const
        fld     TBYTE PTR [rax]
        fstp    TBYTE PTR [rbp-48]
        fld     TBYTE PTR [rbp-48]
        fld     TBYTE PTR [rbp+16]
        fdivp   st(1), st
        fld     TBYTE PTR [rbp-16]
        fmulp   st(1), st
        fstp    TBYTE PTR [rbp-16]
        lea     rax, [rbp-56]
        mov     rdi, rax
        call    __gnu_cxx::__normal_iterator<long double*, std::vector<long double, std::allocator<long double> > >::operator++()
.L100:
        lea     rdx, [rbp-64]
        lea     rax, [rbp-56]
        mov     rsi, rdx
        mov     rdi, rax
        call    bool __gnu_cxx::operator!=<long double*, std::vector<long double, std::allocator<long double> > >(__gnu_cxx::__normal_iterator<long double*, std::vector<long double, std::allocator<long double> > > const&, __gnu_cxx::__normal_iterator<long double*, std::vector<long double, std::allocator<long double> > > const&)
        test    al, al
        jne     .L101
        fld     TBYTE PTR [rbp-16]
        fld     TBYTE PTR [rbp+16]
        fmulp   st(1), st
        leave
        ret
.LC18:
        .string "P_H"
.LC19:
        .string "="
My_Bayes::process_O_H_S(int, int, int):
        push    rbp
        mov     rbp, rsp
        sub     rsp, 288
        mov     QWORD PTR [rbp-248], rdi
        mov     DWORD PTR [rbp-252], esi
        mov     DWORD PTR [rbp-256], edx
        mov     DWORD PTR [rbp-260], ecx
        sub     DWORD PTR [rbp-256], 1
        sub     DWORD PTR [rbp-252], 1
        sub     DWORD PTR [rbp-260], 1
        mov     rax, QWORD PTR [rbp-248]
        lea     rdx, [rax+24]
        mov     eax, DWORD PTR [rbp-252]
        cdqe
        mov     rsi, rax
        mov     rdi, rdx
        call    std::vector<long double, std::allocator<long double> >::operator[](unsigned long)
        fld     TBYTE PTR [rax]
        mov     rax, QWORD PTR [rbp-248]
        lea     rsp, [rsp-16]
        fstp    TBYTE PTR [rsp]
        mov     rdi, rax
        call    My_Bayes::From_O_get_P(long double)
        add     rsp, 16
        fstp    TBYTE PTR [rbp-16]
        mov     esi, OFFSET FLAT:.LC18
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        mov     rdx, rax
        mov     eax, DWORD PTR [rbp-252]
        add     eax, 1
        mov     esi, eax
        mov     rdi, rdx
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(int)
        mov     esi, OFFSET FLAT:.LC19
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        push    QWORD PTR [rbp-8]
        push    QWORD PTR [rbp-16]
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(long double)
        add     rsp, 16
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        mov     rax, QWORD PTR [rbp-248]
        lea     rdx, [rax+24]
        mov     eax, DWORD PTR [rbp-252]
        cdqe
        mov     rsi, rax
        mov     rdi, rdx
        call    std::vector<long double, std::allocator<long double> >::operator[](unsigned long)
        fld     TBYTE PTR [rax]
        fstp    TBYTE PTR [rbp-288]
        mov     rax, QWORD PTR [rbp-248]
        mov     edx, DWORD PTR [rbp-256]
        movsx   rdx, edx
        mov     rsi, rdx
        mov     rdi, rax
        call    std::vector<Rules, std::allocator<Rules> >::operator[](unsigned long)
        mov     rdx, rax
        lea     rax, [rbp-208]
        mov     rsi, rdx
        mov     rdi, rax
        call    Rules::get_LS_LN()
        lea     rdi, [rbp-240]
        mov     rsi, QWORD PTR [rbp-248]
        push    QWORD PTR [rbp-280]
        push    QWORD PTR [rbp-288]
        sub     rsp, 32
        mov     rcx, rsp
        mov     rax, QWORD PTR [rbp-208]
        mov     rdx, QWORD PTR [rbp-200]
        mov     QWORD PTR [rcx], rax
        mov     QWORD PTR [rcx+8], rdx
        mov     rax, QWORD PTR [rbp-192]
        mov     rdx, QWORD PTR [rbp-184]
        mov     QWORD PTR [rcx+16], rax
        mov     QWORD PTR [rcx+24], rdx
        call    My_Bayes::Updated_Bayes_O_HE_O_H_Not_E(std::pair<long double, long double>, long double)
        add     rsp, 48
        fld     TBYTE PTR [rbp-240]
        fstp    TBYTE PTR [rbp-32]
        mov     rax, QWORD PTR [rbp-248]
        push    QWORD PTR [rbp-24]
        push    QWORD PTR [rbp-32]
        mov     rdi, rax
        call    My_Bayes::From_O_get_P(long double)
        add     rsp, 16
        fstp    TBYTE PTR [rbp-48]
        mov     rax, QWORD PTR [rbp-248]
        lea     rdx, [rax+24]
        mov     eax, DWORD PTR [rbp-252]
        cdqe
        mov     rsi, rax
        mov     rdi, rdx
        call    std::vector<long double, std::allocator<long double> >::operator[](unsigned long)
        fld     TBYTE PTR [rax]
        fstp    TBYTE PTR [rbp-288]
        mov     rax, QWORD PTR [rbp-248]
        mov     edx, DWORD PTR [rbp-256]
        movsx   rdx, edx
        mov     rsi, rdx
        mov     rdi, rax
        call    std::vector<Rules, std::allocator<Rules> >::operator[](unsigned long)
        mov     rdx, rax
        lea     rax, [rbp-144]
        mov     rsi, rdx
        mov     rdi, rax
        call    Rules::get_LS_LN()
        lea     rdi, [rbp-176]
        mov     rsi, QWORD PTR [rbp-248]
        push    QWORD PTR [rbp-280]
        push    QWORD PTR [rbp-288]
        sub     rsp, 32
        mov     rcx, rsp
        mov     rax, QWORD PTR [rbp-144]
        mov     rdx, QWORD PTR [rbp-136]
        mov     QWORD PTR [rcx], rax
        mov     QWORD PTR [rcx+8], rdx
        mov     rax, QWORD PTR [rbp-128]
        mov     rdx, QWORD PTR [rbp-120]
        mov     QWORD PTR [rcx+16], rax
        mov     QWORD PTR [rcx+24], rdx
        call    My_Bayes::Updated_Bayes_O_HE_O_H_Not_E(std::pair<long double, long double>, long double)
        add     rsp, 48
        fld     TBYTE PTR [rbp-160]
        fstp    TBYTE PTR [rbp-64]
        mov     rax, QWORD PTR [rbp-248]
        push    QWORD PTR [rbp-56]
        push    QWORD PTR [rbp-64]
        mov     rdi, rax
        call    My_Bayes::From_O_get_P(long double)
        add     rsp, 16
        fstp    TBYTE PTR [rbp-80]
        mov     rax, QWORD PTR [rbp-248]
        lea     rdx, [rax+48]
        mov     eax, DWORD PTR [rbp-260]
        cdqe
        mov     rsi, rax
        mov     rdi, rdx
        call    std::vector<long double, std::allocator<long double> >::operator[](unsigned long)
        fld     TBYTE PTR [rax]
        mov     rax, QWORD PTR [rbp-248]
        lea     rsp, [rsp-16]
        fstp    TBYTE PTR [rsp]
        push    QWORD PTR [rbp-72]
        push    QWORD PTR [rbp-80]
        push    QWORD PTR [rbp-40]
        push    QWORD PTR [rbp-48]
        push    QWORD PTR [rbp-8]
        push    QWORD PTR [rbp-16]
        mov     rdi, rax
        call    My_Bayes::get_P_HS_From_CP_formula(long double, long double, long double, long double)
        add     rsp, 64
        fstp    TBYTE PTR [rbp-96]
        mov     rax, QWORD PTR [rbp-248]
        push    QWORD PTR [rbp-88]
        push    QWORD PTR [rbp-96]
        mov     rdi, rax
        call    My_Bayes::From_P_get_O(long double)
        add     rsp, 16
        fstp    TBYTE PTR [rbp-112]
        fld     TBYTE PTR [rbp-112]
        leave
        ret
.LC20:
        .string "O_H1_S1="
.LC21:
        .string "O_H1_S2="
.LC22:
        .string "O_H1_S1S2="
.LC23:
        .string "P_H2="
.LC24:
        .string "P_H1_S1S2="
.LC25:
        .string "O_H2_H1 ="
.LC26:
        .string "P_H2_H1="
.LC27:
        .string "P_H2_S1S2="
.LC28:
        .string "O_H2_S1S2="
.LC29:
        .string "O_H2_S3="
.LC30:
        .string "--------------------------------------------------------------"
.LC31:
        .string "O_H2_S1S2S3="
My_Bayes::solve_question():
        push    rbp
        mov     rbp, rsp
        push    r15
        push    r14
        push    r13
        push    r12
        push    rbx
        sub     rsp, 584
        mov     QWORD PTR [rbp-600], rdi
        mov     rax, QWORD PTR [rbp-600]
        mov     ecx, 1
        mov     edx, 1
        mov     esi, 1
        mov     rdi, rax
        call    My_Bayes::process_O_H_S(int, int, int)
        fstp    TBYTE PTR [rbp-64]
        mov     esi, OFFSET FLAT:.LC20
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        push    QWORD PTR [rbp-56]
        push    QWORD PTR [rbp-64]
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(long double)
        add     rsp, 16
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        mov     rax, QWORD PTR [rbp-600]
        mov     ecx, 2
        mov     edx, 2
        mov     esi, 1
        mov     rdi, rax
        call    My_Bayes::process_O_H_S(int, int, int)
        fstp    TBYTE PTR [rbp-80]
        mov     esi, OFFSET FLAT:.LC21
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        push    QWORD PTR [rbp-72]
        push    QWORD PTR [rbp-80]
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(long double)
        add     rsp, 16
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        mov     rax, QWORD PTR [rbp-600]
        add     rax, 24
        mov     esi, 0
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::operator[](unsigned long)
        fld     TBYTE PTR [rax]
        fstp    TBYTE PTR [rbp-624]
        fld     TBYTE PTR [rbp-64]
        fstp    TBYTE PTR [rbp-560]
        fld     TBYTE PTR [rbp-80]
        fstp    TBYTE PTR [rbp-544]
        lea     rax, [rbp-560]
        mov     r14, rax
        mov     r15d, 2
        lea     rax, [rbp-513]
        mov     QWORD PTR [rbp-296], rax
        nop
        nop
        lea     rdx, [rbp-513]
        mov     rsi, r14
        mov     rdi, r15
        mov     rcx, r14
        mov     rbx, r15
        mov     rdi, rbx
        lea     rax, [rbp-592]
        mov     rcx, rdx
        mov     rdx, rdi
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::vector(std::initializer_list<long double>, std::allocator<long double> const&) [complete object constructor]
        lea     rdx, [rbp-592]
        mov     rax, QWORD PTR [rbp-600]
        push    QWORD PTR [rbp-616]
        push    QWORD PTR [rbp-624]
        mov     rsi, rdx
        mov     rdi, rax
        call    My_Bayes::Get_Posterior_Probability_From_All_Observation(std::vector<long double, std::allocator<long double> >, long double)
        add     rsp, 16
        fstp    TBYTE PTR [rbp-96]
        lea     rax, [rbp-592]
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::~vector() [complete object destructor]
        lea     rax, [rbp-513]
        mov     rdi, rax
        call    std::__new_allocator<long double>::~__new_allocator() [base object destructor]
        nop
        mov     esi, OFFSET FLAT:.LC22
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        push    QWORD PTR [rbp-88]
        push    QWORD PTR [rbp-96]
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(long double)
        add     rsp, 16
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        mov     rax, QWORD PTR [rbp-600]
        add     rax, 24
        mov     esi, 1
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::operator[](unsigned long)
        fld     TBYTE PTR [rax]
        fstp    TBYTE PTR [rbp-112]
        mov     rax, QWORD PTR [rbp-600]
        push    QWORD PTR [rbp-104]
        push    QWORD PTR [rbp-112]
        mov     rdi, rax
        call    My_Bayes::From_O_get_P(long double)
        add     rsp, 16
        fstp    TBYTE PTR [rbp-128]
        mov     esi, OFFSET FLAT:.LC23
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        push    QWORD PTR [rbp-120]
        push    QWORD PTR [rbp-128]
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(long double)
        add     rsp, 16
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        mov     rax, QWORD PTR [rbp-600]
        push    QWORD PTR [rbp-88]
        push    QWORD PTR [rbp-96]
        mov     rdi, rax
        call    My_Bayes::From_O_get_P(long double)
        add     rsp, 16
        fstp    TBYTE PTR [rbp-144]
        mov     esi, OFFSET FLAT:.LC24
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        push    QWORD PTR [rbp-136]
        push    QWORD PTR [rbp-144]
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(long double)
        add     rsp, 16
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        mov     rax, QWORD PTR [rbp-600]
        mov     esi, 2
        mov     rdi, rax
        call    std::vector<Rules, std::allocator<Rules> >::operator[](unsigned long)
        mov     rdx, rax
        lea     rax, [rbp-480]
        mov     rsi, rdx
        mov     rdi, rax
        call    Rules::get_LS_LN()
        lea     rdi, [rbp-512]
        mov     rsi, QWORD PTR [rbp-600]
        push    QWORD PTR [rbp-104]
        push    QWORD PTR [rbp-112]
        sub     rsp, 32
        mov     rcx, rsp
        mov     rax, QWORD PTR [rbp-480]
        mov     rdx, QWORD PTR [rbp-472]
        mov     QWORD PTR [rcx], rax
        mov     QWORD PTR [rcx+8], rdx
        mov     rax, QWORD PTR [rbp-464]
        mov     rdx, QWORD PTR [rbp-456]
        mov     QWORD PTR [rcx+16], rax
        mov     QWORD PTR [rcx+24], rdx
        call    My_Bayes::Updated_Bayes_O_HE_O_H_Not_E(std::pair<long double, long double>, long double)
        add     rsp, 48
        fld     TBYTE PTR [rbp-512]
        fstp    TBYTE PTR [rbp-160]
        mov     esi, OFFSET FLAT:.LC25
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        push    QWORD PTR [rbp-152]
        push    QWORD PTR [rbp-160]
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(long double)
        add     rsp, 16
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        mov     rax, QWORD PTR [rbp-600]
        mov     esi, 2
        mov     rdi, rax
        call    std::vector<Rules, std::allocator<Rules> >::operator[](unsigned long)
        mov     rdx, rax
        lea     rax, [rbp-416]
        mov     rsi, rdx
        mov     rdi, rax
        call    Rules::get_LS_LN()
        lea     rdi, [rbp-448]
        mov     rsi, QWORD PTR [rbp-600]
        push    QWORD PTR [rbp-104]
        push    QWORD PTR [rbp-112]
        sub     rsp, 32
        mov     rcx, rsp
        mov     rax, QWORD PTR [rbp-416]
        mov     rdx, QWORD PTR [rbp-408]
        mov     QWORD PTR [rcx], rax
        mov     QWORD PTR [rcx+8], rdx
        mov     rax, QWORD PTR [rbp-400]
        mov     rdx, QWORD PTR [rbp-392]
        mov     QWORD PTR [rcx+16], rax
        mov     QWORD PTR [rcx+24], rdx
        call    My_Bayes::Updated_Bayes_O_HE_O_H_Not_E(std::pair<long double, long double>, long double)
        add     rsp, 48
        fld     TBYTE PTR [rbp-432]
        fstp    TBYTE PTR [rbp-176]
        mov     rax, QWORD PTR [rbp-600]
        push    QWORD PTR [rbp-152]
        push    QWORD PTR [rbp-160]
        mov     rdi, rax
        call    My_Bayes::From_O_get_P(long double)
        add     rsp, 16
        fstp    TBYTE PTR [rbp-192]
        mov     esi, OFFSET FLAT:.LC26
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        push    QWORD PTR [rbp-184]
        push    QWORD PTR [rbp-192]
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(long double)
        add     rsp, 16
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        mov     rax, QWORD PTR [rbp-600]
        push    QWORD PTR [rbp-168]
        push    QWORD PTR [rbp-176]
        mov     rdi, rax
        call    My_Bayes::From_O_get_P(long double)
        add     rsp, 16
        fstp    TBYTE PTR [rbp-208]
        mov     rax, QWORD PTR [rbp-600]
        add     rax, 24
        mov     esi, 0
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::operator[](unsigned long)
        fld     TBYTE PTR [rax]
        mov     rax, QWORD PTR [rbp-600]
        lea     rsp, [rsp-16]
        fstp    TBYTE PTR [rsp]
        mov     rdi, rax
        call    My_Bayes::From_O_get_P(long double)
        add     rsp, 16
        fstp    TBYTE PTR [rbp-224]
        mov     rax, QWORD PTR [rbp-600]
        push    QWORD PTR [rbp-200]
        push    QWORD PTR [rbp-208]
        push    QWORD PTR [rbp-184]
        push    QWORD PTR [rbp-192]
        push    QWORD PTR [rbp-136]
        push    QWORD PTR [rbp-144]
        push    QWORD PTR [rbp-216]
        push    QWORD PTR [rbp-224]
        push    QWORD PTR [rbp-120]
        push    QWORD PTR [rbp-128]
        mov     rdi, rax
        call    My_Bayes::get_P_HS_from_EH_Linear_Interpolation(long double, long double, long double, long double, long double)
        add     rsp, 80
        fstp    TBYTE PTR [rbp-240]
        mov     esi, OFFSET FLAT:.LC27
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        push    QWORD PTR [rbp-232]
        push    QWORD PTR [rbp-240]
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(long double)
        add     rsp, 16
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        mov     rax, QWORD PTR [rbp-600]
        push    QWORD PTR [rbp-232]
        push    QWORD PTR [rbp-240]
        mov     rdi, rax
        call    My_Bayes::From_P_get_O(long double)
        add     rsp, 16
        fstp    TBYTE PTR [rbp-256]
        mov     esi, OFFSET FLAT:.LC28
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        push    QWORD PTR [rbp-248]
        push    QWORD PTR [rbp-256]
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(long double)
        add     rsp, 16
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        mov     rax, QWORD PTR [rbp-600]
        mov     ecx, 3
        mov     edx, 4
        mov     esi, 2
        mov     rdi, rax
        call    My_Bayes::process_O_H_S(int, int, int)
        fstp    TBYTE PTR [rbp-272]
        mov     esi, OFFSET FLAT:.LC29
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        push    QWORD PTR [rbp-264]
        push    QWORD PTR [rbp-272]
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(long double)
        add     rsp, 16
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        fld     TBYTE PTR [rbp-256]
        fstp    TBYTE PTR [rbp-352]
        fld     TBYTE PTR [rbp-272]
        fstp    TBYTE PTR [rbp-336]
        lea     rax, [rbp-352]
        mov     r12, rax
        mov     r13d, 2
        lea     rax, [rbp-305]
        mov     QWORD PTR [rbp-304], rax
        nop
        nop
        lea     rdx, [rbp-305]
        mov     rsi, r12
        mov     rdi, r13
        mov     rcx, r12
        mov     rbx, r13
        mov     rdi, rbx
        lea     rax, [rbp-384]
        mov     rcx, rdx
        mov     rdx, rdi
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::vector(std::initializer_list<long double>, std::allocator<long double> const&) [complete object constructor]
        lea     rdx, [rbp-384]
        mov     rax, QWORD PTR [rbp-600]
        push    QWORD PTR [rbp-104]
        push    QWORD PTR [rbp-112]
        mov     rsi, rdx
        mov     rdi, rax
        call    My_Bayes::Get_Posterior_Probability_From_All_Observation(std::vector<long double, std::allocator<long double> >, long double)
        add     rsp, 16
        fstp    TBYTE PTR [rbp-288]
        lea     rax, [rbp-384]
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::~vector() [complete object destructor]
        lea     rax, [rbp-305]
        mov     rdi, rax
        call    std::__new_allocator<long double>::~__new_allocator() [base object destructor]
        nop
        mov     esi, OFFSET FLAT:.LC30
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        mov     esi, OFFSET FLAT:.LC31
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        push    QWORD PTR [rbp-280]
        push    QWORD PTR [rbp-288]
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(long double)
        add     rsp, 16
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        mov     esi, OFFSET FLAT:.LC30
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        mov     esi, OFFSET FLAT:_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
        mov     rdi, rax
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(std::basic_ostream<char, std::char_traits<char> >& (*)(std::basic_ostream<char, std::char_traits<char> >&))
        fld     TBYTE PTR [rbp-288]
        jmp     .L111
        mov     rbx, rax
        lea     rax, [rbp-513]
        mov     rdi, rax
        call    std::__new_allocator<long double>::~__new_allocator() [base object destructor]
        nop
        mov     rax, rbx
        mov     rdi, rax
        call    _Unwind_Resume
        mov     rbx, rax
        lea     rax, [rbp-305]
        mov     rdi, rax
        call    std::__new_allocator<long double>::~__new_allocator() [base object destructor]
        nop
        mov     rax, rbx
        mov     rdi, rax
        call    _Unwind_Resume
.L111:
        lea     rsp, [rbp-40]
        pop     rbx
        pop     r12
        pop     r13
        pop     r14
        pop     r15
        pop     rbp
        ret
My_Bayes::~My_Bayes() [base object destructor]:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        mov     QWORD PTR [rbp-8], rdi
        mov     rax, QWORD PTR [rbp-8]
        add     rax, 48
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::~vector() [complete object destructor]
        mov     rax, QWORD PTR [rbp-8]
        add     rax, 24
        mov     rdi, rax
        call    std::vector<long double, std::allocator<long double> >::~vector() [complete object destructor]
        mov     rax, QWORD PTR [rbp-8]
        mov     rdi, rax
        call    std::vector<Rules, std::allocator<Rules> >::~vector() [complete object destructor]
        nop
        leave
        ret
main:
        push    rbp
        mov     rbp, rsp
        push    rbx
        sub     rsp, 88
        lea     rax, [rbp-96]
        mov     rdi, rax
        call    My_Bayes::My_Bayes() [complete object constructor]
        lea     rax, [rbp-96]
        mov     rdi, rax
        call    My_Bayes::solve_question()
        fstp    st(0)
        mov     ebx, 0
        lea     rax, [rbp-96]
        mov     rdi, rax
        call    My_Bayes::~My_Bayes() [complete object destructor]
        mov     eax, ebx
        jmp     .L117
        mov     rbx, rax
        lea     rax, [rbp-96]
        mov     rdi, rax
        call    My_Bayes::~My_Bayes() [complete object destructor]
        mov     rax, rbx
        mov     rdi, rax
        call    _Unwind_Resume
.L117:
        mov     rbx, QWORD PTR [rbp-8]
        leave
        ret
.LC32:
        .string "basic_string: construction from null is not valid"
.LC33:
        .string "vector::_M_realloc_insert"
.LC34:
        .string "cannot create std::vector larger than max_size()"
Rules::Rules(Rules&&) [base object constructor]:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        mov     QWORD PTR [rbp-8], rdi
        mov     QWORD PTR [rbp-16], rsi
        mov     rax, QWORD PTR [rbp-8]
        mov     rdx, QWORD PTR [rbp-16]
        mov     rsi, rdx
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::basic_string(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&) [complete object constructor]
        mov     rax, QWORD PTR [rbp-8]
        add     rax, 32
        mov     rdx, QWORD PTR [rbp-16]
        add     rdx, 32
        mov     rsi, rdx
        mov     rdi, rax
        call    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::basic_string(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&) [complete object constructor]
        mov     rax, QWORD PTR [rbp-16]
        fld     TBYTE PTR [rax+64]
        mov     rax, QWORD PTR [rbp-8]
        fstp    TBYTE PTR [rax+64]
        mov     rax, QWORD PTR [rbp-16]
        fld     TBYTE PTR [rax+80]
        mov     rax, QWORD PTR [rbp-8]
        fstp    TBYTE PTR [rax+80]
        nop
        leave
        ret
.LC17:
        .long   -858992640
        .long   -858993460
        .long   16380
        .long   0