import cv2
import numpy
import math
from enum import Enum

class RefBallHatchDetection:
    """
    An OpenCV pipeline generated by GRIP.
    """
    
    def __init__(self):
        """initializes all values to presets or None if need to be set
        """

        self.__blur_0_type = BlurType.Box_Blur
        self.__blur_0_radius = 5.838660578386605

        self.blur_0_output = None

        self.__hsv_threshold_0_input = self.blur_0_output
        self.__hsv_threshold_0_hue = [49.511978704525276, 69.82758620689656]
        self.__hsv_threshold_0_saturation = [90.50576752440105, 129.69827586206895]
        self.__hsv_threshold_0_value = [121.05146406388641, 190.15086206896552]

        self.hsv_threshold_0_output = None

        self.__find_lines_input = self.hsv_threshold_0_output

        self.find_lines_output = None

        self.__filter_lines_lines = self.find_lines_output
        self.__filter_lines_min_length = 20.0
        self.__filter_lines_angle = [6.388642413487134, 360.0]

        self.filter_lines_output = None

        self.__hsv_threshold_1_input = self.blur_0_output
        self.__hsv_threshold_1_hue = [15.173025732031942, 20.172413793103456]
        self.__hsv_threshold_1_saturation = [179.33303085299454, 255.0]
        self.__hsv_threshold_1_value = [185.92385466772524, 255.0]

        self.hsv_threshold_1_output = None

        self.__blur_1_input = self.hsv_threshold_1_output
        self.__blur_1_type = BlurType.Median_Filter
        self.__blur_1_radius = 10.909090909090908

        self.blur_1_output = None

        self.__find_contours_0_input = self.hsv_threshold_1_output
        self.__find_contours_0_external_only = False

        self.find_contours_0_output = None

        self.__hsv_threshold_2_input = self.blur_0_output
        self.__hsv_threshold_2_hue = [24.39024390243902, 37.105263157894754]
        self.__hsv_threshold_2_saturation = [198.10298102981028, 255.0]
        self.__hsv_threshold_2_value = [195.41085991928335, 255.0]

        self.hsv_threshold_2_output = None

        self.__blur_2_input = self.hsv_threshold_2_output
        self.__blur_2_type = BlurType.Box_Blur
        self.__blur_2_radius = 14.553990610328638

        self.blur_2_output = None

        self.__find_contours_1_input = self.blur_2_output
        self.__find_contours_1_external_only = False

        self.find_contours_1_output = None

        self.__filter_contours_contours = self.find_contours_1_output
        self.__filter_contours_min_area = 0
        self.__filter_contours_min_perimeter = 0
        self.__filter_contours_min_width = 800.0
        self.__filter_contours_max_width = 1010.0
        self.__filter_contours_min_height = 0
        self.__filter_contours_max_height = 1000
        self.__filter_contours_solidity = [0.0, 100.0]
        self.__filter_contours_max_vertices = 1000000
        self.__filter_contours_min_vertices = 0
        self.__filter_contours_min_ratio = 0
        self.__filter_contours_max_ratio = 1000

        self.filter_contours_output = None


    def process(self, source0):
        """
        Runs the pipeline and sets all outputs to new values.
        """
        # Step Blur0:
        self.__blur_0_input = source0
        (self.blur_0_output) = self.__blur(self.__blur_0_input, self.__blur_0_type, self.__blur_0_radius)

        # Step HSV_Threshold0:
        self.__hsv_threshold_0_input = self.blur_0_output
        (self.hsv_threshold_0_output) = self.__hsv_threshold(self.__hsv_threshold_0_input, self.__hsv_threshold_0_hue, self.__hsv_threshold_0_saturation, self.__hsv_threshold_0_value)

        # Step Find_Lines0:
        self.__find_lines_input = self.hsv_threshold_0_output
        (self.find_lines_output) = self.__find_lines(self.__find_lines_input)

        # Step Filter_Lines0:
        self.__filter_lines_lines = self.find_lines_output
        (self.filter_lines_output) = self.__filter_lines(self.__filter_lines_lines, self.__filter_lines_min_length, self.__filter_lines_angle)

        # Step HSV_Threshold1:
        self.__hsv_threshold_1_input = self.blur_0_output
        (self.hsv_threshold_1_output) = self.__hsv_threshold(self.__hsv_threshold_1_input, self.__hsv_threshold_1_hue, self.__hsv_threshold_1_saturation, self.__hsv_threshold_1_value)

        # Step Blur1:
        self.__blur_1_input = self.hsv_threshold_1_output
        (self.blur_1_output) = self.__blur(self.__blur_1_input, self.__blur_1_type, self.__blur_1_radius)

        # Step Find_Contours0:
        self.__find_contours_0_input = self.hsv_threshold_1_output
        (self.find_contours_0_output) = self.__find_contours(self.__find_contours_0_input, self.__find_contours_0_external_only)

        # Step HSV_Threshold2:
        self.__hsv_threshold_2_input = self.blur_0_output
        (self.hsv_threshold_2_output) = self.__hsv_threshold(self.__hsv_threshold_2_input, self.__hsv_threshold_2_hue, self.__hsv_threshold_2_saturation, self.__hsv_threshold_2_value)

        # Step Blur2:
        self.__blur_2_input = self.hsv_threshold_2_output
        (self.blur_2_output) = self.__blur(self.__blur_2_input, self.__blur_2_type, self.__blur_2_radius)

        # Step Find_Contours1:
        self.__find_contours_1_input = self.blur_2_output
        (self.find_contours_1_output) = self.__find_contours(self.__find_contours_1_input, self.__find_contours_1_external_only)

        # Step Filter_Contours0:
        self.__filter_contours_contours = self.find_contours_1_output
        (self.filter_contours_output) = self.__filter_contours(self.__filter_contours_contours, self.__filter_contours_min_area, self.__filter_contours_min_perimeter, self.__filter_contours_min_width, self.__filter_contours_max_width, self.__filter_contours_min_height, self.__filter_contours_max_height, self.__filter_contours_solidity, self.__filter_contours_max_vertices, self.__filter_contours_min_vertices, self.__filter_contours_min_ratio, self.__filter_contours_max_ratio)


    class Line:

        def __init__(self, x1, y1, x2, y2):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2

        def length(self):
            return numpy.sqrt(pow(self.x2 - self.x1, 2) + pow(self.y2 - self.y1, 2))

        def angle(self):
            return math.degrees(math.atan2(self.y2 - self.y1, self.x2 - self.x1))
    @staticmethod
    def __find_lines(input):
        """Finds all line segments in an image.
        Args:
            input: A numpy.ndarray.
        Returns:
            A filtered list of Lines.
        """
        detector = cv2.createLineSegmentDetector()
        if (len(input.shape) == 2 or input.shape[2] == 1):
            lines = detector.detect(input)
        else:
            tmp = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
            lines = detector.detect(tmp)
        output = []
        if len(lines) != 0:
            for i in range(1, len(lines[0])):
                tmp = RefBallHatchDetecion.Line(lines[0][i, 0][0], lines[0][i, 0][1],
                                lines[0][i, 0][2], lines[0][i, 0][3])
                output.append(tmp)
        return output

    @staticmethod
    def __filter_lines(inputs, min_length, angle):
        """Filters out lines that do not meet certain criteria.
        Args:
            inputs: A list of Lines.
            min_Lenght: The minimum lenght that will be kept.
            angle: The minimum and maximum angles in degrees as a list of two numbers.
        Returns:
            A filtered list of Lines.
        """
        outputs = []
        for line in inputs:
            if (line.length() > min_length):
                if ((line.angle() >= angle[0] and line.angle() <= angle[1]) or
                        (line.angle() + 180.0 >= angle[0] and line.angle() + 180.0 <= angle[1])):
                    outputs.append(line)
        return outputs

    @staticmethod
    def __hsv_threshold(input, hue, sat, val):
        """Segment an image based on hue, saturation, and value ranges.
        Args:
            input: A BGR numpy.ndarray.
            hue: A list of two numbers the are the min and max hue.
            sat: A list of two numbers the are the min and max saturation.
            lum: A list of two numbers the are the min and max value.
        Returns:
            A black and white numpy.ndarray.
        """
        out = cv2.cvtColor(input, cv2.COLOR_BGR2HSV)
        return cv2.inRange(out, (hue[0], sat[0], val[0]),  (hue[1], sat[1], val[1]))

    @staticmethod
    def __blur(src, type, radius):
        """Softens an image using one of several filters.
        Args:
            src: The source mat (numpy.ndarray).
            type: The blurType to perform represented as an int.
            radius: The radius for the blur as a float.
        Returns:
            A numpy.ndarray that has been blurred.
        """
        if(type is BlurType.Box_Blur):
            ksize = int(2 * round(radius) + 1)
            return cv2.blur(src, (ksize, ksize))
        elif(type is BlurType.Gaussian_Blur):
            ksize = int(6 * round(radius) + 1)
            return cv2.GaussianBlur(src, (ksize, ksize), round(radius))
        elif(type is BlurType.Median_Filter):
            ksize = int(2 * round(radius) + 1)
            return cv2.medianBlur(src, ksize)
        else:
            return cv2.bilateralFilter(src, -1, round(radius), round(radius))

    @staticmethod
    def __find_contours(input, external_only):
        """Sets the values of pixels in a binary image to their distance to the nearest black pixel.
        Args:
            input: A numpy.ndarray.
            external_only: A boolean. If true only external contours are found.
        Return:
            A list of numpy.ndarray where each one represents a contour.
        """
        if(external_only):
            mode = cv2.RETR_EXTERNAL
        else:
            mode = cv2.RETR_LIST
        method = cv2.CHAIN_APPROX_SIMPLE
        im2, contours, hierarchy =cv2.findContours(input, mode=mode, method=method)
        return contours

    @staticmethod
    def __filter_contours(input_contours, min_area, min_perimeter, min_width, max_width,
                        min_height, max_height, solidity, max_vertex_count, min_vertex_count,
                        min_ratio, max_ratio):
        """Filters out contours that do not meet certain criteria.
        Args:
            input_contours: Contours as a list of numpy.ndarray.
            min_area: The minimum area of a contour that will be kept.
            min_perimeter: The minimum perimeter of a contour that will be kept.
            min_width: Minimum width of a contour.
            max_width: MaxWidth maximum width.
            min_height: Minimum height.
            max_height: Maximimum height.
            solidity: The minimum and maximum solidity of a contour.
            min_vertex_count: Minimum vertex Count of the contours.
            max_vertex_count: Maximum vertex Count.
            min_ratio: Minimum ratio of width to height.
            max_ratio: Maximum ratio of width to height.
        Returns:
            Contours as a list of numpy.ndarray.
        """
        output = []
        for contour in input_contours:
            x,y,w,h = cv2.boundingRect(contour)
            if (w < min_width or w > max_width):
                continue
            if (h < min_height or h > max_height):
                continue
            area = cv2.contourArea(contour)
            if (area < min_area):
                continue
            if (cv2.arcLength(contour, True) < min_perimeter):
                continue
            hull = cv2.convexHull(contour)
            solid = 100 * area / cv2.contourArea(hull)
            if (solid < solidity[0] or solid > solidity[1]):
                continue
            if (len(contour) < min_vertex_count or len(contour) > max_vertex_count):
                continue
            ratio = (float)(w) / h
            if (ratio < min_ratio or ratio > max_ratio):
                continue
            output.append(contour)
        return output


BlurType = Enum('BlurType', 'Box_Blur Gaussian_Blur Median_Filter Bilateral_Filter')

