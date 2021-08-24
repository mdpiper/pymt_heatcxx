#! /usr/bin/env python
import pkg_resources

__version__ = pkg_resources.get_distribution("pymt_heatcxx").version


from .bmi import HeatModel

__all__ = [
    "HeatModel",
]
