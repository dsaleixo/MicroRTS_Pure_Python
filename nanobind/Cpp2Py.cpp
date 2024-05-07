#include <nanobind/nanobind.h>

namespace nb = nanobind;

nb::list double_it(nb::list l) {
    nb::list result;
    for (nb::handle h : l)
        result.append(h * nb::int_(2));
    return result;
}

NB_MODULE(Cpp2Py, m) {
    m.def("double_it", &double_it);
}