class Solution:
    def trap(self, height: List[int]) -> int:
        if height == []:
            return 0

        # height, how many we ate, height penalty
        stack = [[height[0], 0, 0]]
        area = 0

        for h in height[1:]:
            elem = [h, 0, 0]
            largest = 0

            while len(stack) > 0:
                if elem[0] >= stack[-1][0]:
                    r_elem = stack.pop()

                    largest = r_elem[0]
                    elem[1] += r_elem[1] + 1
                    elem[2] += r_elem[0] + r_elem[2]
                else:
                    break

            if len(stack) > 0:
                largest = elem[0]

            area_d = largest * elem[1] - elem[2]

            area += area_d
            elem[2] += area_d

            if len(stack) == 0:
                elem[1] = 0
                elem[2] = 0

            stack.append(elem)

        return area
