# Healing Power Algorithm
# For Rank 9 Healing Wave
R9_Healing_Wave = {
    "lower_limit":1527,
    "upper_limit":1742,
    "cast_time":3
}
R7_Healing_Wave ={
    "lower_limit":835,
    "upper_limit":961,
    "cast_time":3
}
def actual_power(dict_name, healing_power=0):
    spell = dict_name
    base_power = ((spell["lower_limit"] + spell["upper_limit"]) / 2)
    direct_coefficient = (spell["cast_time"] / 3.5)
    actual_power = base_power + healing_power * direct_coefficient
    return actual_power


actual_power(R9_Healing_Wave, 418)
#returns 1992.78 (90 total healing increase)
actual_power(R9_Healing_Wave, 313)
#returns 1902.78 
actual_power(R7_Healing_Wave, 418)
#returns 1256.28 (90 total healing increase)
actual_power(R7_Healing_Wave, 313)
#returns 1166.28