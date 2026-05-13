class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        g_truck=0
        m_truck=0
        p_truck=0
        g_index=0
        p_index=[]
        m_index=[]
        for i in range(len(garbage)):
            if "G" in garbage[i]:
                g_truck += garbage[i].count('G')
                g_index=i
            if "P" in garbage[i]:
                p_truck += garbage[i].count('P')
                p_index=i
            if "M" in garbage[i]:
                m_truck += garbage[i].count('M')
                m_index=i
        total_count=0

        if g_truck!=0:
            total_count+=g_truck
            total_count+=sum(travel[:g_index])
        if p_truck!=0:
            total_count+=p_truck
            total_count+=sum(travel[:p_index])
        if m_truck!=0:
            total_count+=m_truck
            total_count+=sum(travel[:m_index])
        return total_count
            
            
