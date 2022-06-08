import math


class EuclideanDistTracker:
    def __init__(self):

        # Store the center positions of the objects

        self.center_points = {}

        # Keep the count of the IDs
        # Each time a new object id detected, the count will increase by one

        self.id_count = 0

    def update(self, objects_rect):

        # Objects boxes and ids

        objects_bbs_ids = []

        # Get the center point of new object

        for rect in objects_rect:
            x, y, w, h = rect
            fx = 2*x
            fxt = fx + w

            fy = 2*y
            fyt = fy + h

            bx = fxt // 2
            by = fyt //2

            cx = bx
            cy = by

            # Find out if that object was detected already

            var = False
            same_object_detected = var

            for id, pt in self.center_points.items():

                # New variables for 'for' condition

                var_cx = cx
                var_cy = cy
                dist = math.hypot(var_cx - pt[0], var_cy - pt[1])

                if dist < 25:

                    # New variables for if condition

                    var_ifcx = cx
                    var_ifcy = cy

                    self.center_points[id] = (var_ifcx, var_ifcy)
                    print(self.center_points)

                    # Rename all variables for if condition

                    var_x = x
                    var_y = y
                    var_w = w
                    var_h = h

                    objects_bbs_ids.append([var_x, var_y, var_w, var_h, id])
                    same_object_detected = True
                    break

            # New object is detected we assign the ID to that object

            if same_object_detected is False:

                # For the second if condition

                sec_cx = cx
                sec_cy = cy

                self.center_points[self.id_count] = (sec_cx, sec_cy)

                sec_x = x
                sec_y = y
                sec_w = w
                sec_h = h

                objects_bbs_ids.append([sec_x, sec_y, sec_w, sec_h, self.id_count])

                added = 1
                self.id_count = self.id_count + added

        # Clean the dictionary by center points to remove IDS not used anymore

        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center

        # Update dictionary with IDs not used removed
        
        self.center_points = new_center_points.copy()
        
        # Return the value

        return objects_bbs_ids
