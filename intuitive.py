import sys


def degrees_to_voltage(degrees):
    """
    Converts the input in degrees to a voltage value
    :param degrees: Shaft position in degrees
    :return: float: Expected reading in voltage
    """
    slope = 5.0 / 360.
    fractional_degree = degrees % 360.
    return slope * fractional_degree  # y = slope * x linear equation


def voltage_to_degrees(voltage_value):
    """
    Converts the input voltage value  to degrees
    :param voltage_value: Analog voltage value
    :return: float: Degrees that would cause this voltage
    """
    slope = 360.0 / 5.0
    return slope * voltage_value  # y = slope * x linear equation


def quadrature_decoder(encoder_value):
    """
    Decoded the input decode value
    :param encoder_value: Signed integer value from the encoder
    :return: float: Actual degrees in conversion
    """
    degrees = (encoder_value * 360.) / 2048 / 30  # 2048 counts per revolutions with 30:1 gear reduction
    degrees % 360.
    return degrees


def potentionmeter_DAC(adc_value):
    """
    Coverts the ADC digital value back to analog
    :param adc_value: Digital value which is 8 bit so value of 0 is 0V and value of 255 is 5V.
    :return: float: Analog value of the digital input
    """
    resolution = 5.0 / ((2 ** 8) - 1)
    return resolution * adc_value


def almost_equal(float_num1, float_num2):
    """
    Comparing two floating point numbers for equality
    :param float_num1: First float number
    :param float_num2: Second float number
    :return: boolean True if they are difference is less than 0.1 (99% accuracy)
    """
    return round(abs(float_num1 - float_num2)) < 0.1


if __name__ == "__main__":
    filename = sys.argv[1]
    offset_degree = 0.0
    for line in open(filename):
        time, encoder_data, potentiometer_data = line.split()
        if float(time) > 0.5:
            if float(time) == 0.501:  # expect at this time the system is calibrated so calculating the offset
                first_potentiometer_read = potentionmeter_DAC(float(potentiometer_data))
                first_encoder_data = quadrature_decoder(abs(float(encoder_data)))
                offset_degree = first_encoder_data - voltage_to_degrees(first_potentiometer_read)
            current_encoder_data = quadrature_decoder(abs(float(encoder_data)))
            current_potentiometer_output = potentionmeter_DAC(float(potentiometer_data))
            if float(encoder_data) < 0:  # this means the now the degree is going below initial position
                current_encoder_data = abs(offset_degree) - current_encoder_data
            else:
                current_encoder_data = abs(offset_degree) + current_encoder_data
            if current_encoder_data > 360:
                current_encoder_data %= 360.
            expected_voltage = degrees_to_voltage(abs(current_encoder_data))
            if not almost_equal(expected_voltage, current_potentiometer_output):
                print "Erroneous reading at Time: {}".format(time)
