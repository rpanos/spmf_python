


# 254,255 ==> 349 #SUP: 22 #CONF: 0.4230769230769231 #LIFT: 2.036410256410256
def parse_line(spmf_output_line):

    if not spmf_output_line or len(spmf_output_line) == 1:
        return None

    rule_stats = spmf_output_line.split('#SUP:')
    if not rule_stats or len(rule_stats) != 2:
        print " no SUP"
        return None

    rule_halfs = rule_stats[0].split('==>')
    if not rule_halfs or len(rule_halfs) != 2:
        print " no ==>"
        return None

    if ',' in rule_halfs[0]:
        antcedants_str = rule_halfs[0].split(',')
    else:
        antcedants_str = [rule_halfs[0]]
    antcedants_int = [int(antcedant_str) for antcedant_str in antcedants_str]

    if ',' in rule_halfs[1]:
        consequents_str = rule_halfs[1].split(',')
    else:
        consequents_str = [rule_halfs[1]]
    consequents_int = [int(consequent_str) for consequent_str in consequents_str]

    stat_str = rule_stats[1]
    stats = {}
    if "#LIFT:" in stat_str:
        lift_str = stat_str[stat_str.index("#LIFT:") + 6:]
        stats['lift'] = float(lift_str)
        stat_str = stat_str[:stat_str.index("#LIFT:")]

    if "#CONF:" in stat_str:
        conf_str = stat_str[stat_str.index("#CONF:") + 6:]
        stats['conf'] = float(conf_str)
        stat_str = stat_str[:stat_str.index("#CONF:")]

    stats['supp'] = float(stat_str)

    return (antcedants_int, consequents_int, stats)



if __name__=='__main__':

    print str(parse_line('254,255 ==> 349 #SUP: 22 #CONF: 0.4230769230769231 #LIFT: 2.036410256410256'))