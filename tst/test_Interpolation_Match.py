import allure
import pytest

from .main import *

x0 = 0
x1 = 100
y0 = 0
y1 = 5


@pytest.mark.parametrize("x", range(101))
@allure.feature(
    """
        Steps:\
        Step1: Have the source files ready for generating binary for swc_fast_charge.,\
        Step2: Generate binary (shared dll using cmake) using cmake,\
        Step3: calculate AFC_interp,  HSD_interp from input x range from 0 to 101,\
        Step4: compare output with expected value from input param - Le_I_Stg_ChgCurr,\
        Step5: Test result should match AFC_interp == HSD_interp,\

        parent_suite: swc_fast_charge
        suite: afc_interpolation_match
        sub_suite: interpolation_equations
        label: UnitTest
    """
)
def test_interpolation_equations(x):
    """
    This test verifies the interpolation equations
    """
    AFC_interp = y0 + (((x - x0) * (y1 - y0)) / (x1 - x0))
    HSD_interp = ((y0 * (x1 - x)) + (y1 * (x - x0))) / (x1 - x0)
    logger.info(f"ACTUAL: {HSD_interp}, EXPECTED={AFC_interp}")
    assert (
        AFC_interp == HSD_interp
    ), f"Interpolation equations do not match for x={x}, x0={x0}, x1={x1}, y0={y0}, y1={y1}"
