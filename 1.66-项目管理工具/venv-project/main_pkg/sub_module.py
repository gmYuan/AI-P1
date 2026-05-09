from .utils import add

# ImportError:
# attempted relative import with no known parent package
# .utils写法只能在包里面使用
# python -m main_pkg.sub_module
print(add(1, 2))
