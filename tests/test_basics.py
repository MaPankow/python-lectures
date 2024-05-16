import math
import unittest

from exercises.basics import *

class TestBasics(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 5), 8)

    def test_subtract(self):
        self.assertEqual(subtract(8, 5), 3)

    def test_multiply(self):
        self.assertEqual(multiply(4, 6), 24)

    def test_divide(self):
        self.assertEqual(divide(12, 4), 3)

    def test_in_fahrenheit(self):
        self.assertEqual(inFahrenheit(0), 32)

    def test_in_celsius(self):
        self.assertEqual(inCelsius(32), 0)
        self.assertAlmostEqual(inCelsius(0), -17.77777777777778)

    def test_umsatzsteuer_2005_18k(self):
        self.assertEqual(umsatzsteuer(18000, 2005), 3420)
    
    def test_umsatzsteuer_2020_10k(self):
        self.assertEqual(umsatzsteuer(10000, 2020), 0)

    def test_umsatzsteuer_2020_100k(self):
        self.assertEqual(umsatzsteuer(100000, 2020), 19000)

    def test_umsatzsteuer_2023_18k(self):
        self.assertEqual(umsatzsteuer(18000, 2023), 0)

    def test_area_of_unit_circle(self):
        self.assertAlmostEqual(area('circle', { 'radius': 1.0 }), math.pi)

    def test_area_of_triangle(self):
        self.assertEqual(area('triangle', { 'base': 2, 'height': 1.8 }), 1.8)

    def test_area_of_rectangle(self):
        self.assertEqual(area('rectangle', { 'base': 2, 'height': 1.8 }), 3.6)

    def test_fizzbuzz(self):
        '''
        test('FizzBuzz', () => {
            const consoleMock = vi.spyOn(console, 'log').mockImplementation(() => undefined)
            
            afterAll(consoleMock.mockReset)

            fizzbuzz(10)

            expect(consoleMock).toHaveBeenCalledWith(1)
            expect(consoleMock).toHaveBeenCalledWith(2)
            expect(consoleMock).toHaveBeenCalledWith('fizz')
            expect(consoleMock).toHaveBeenCalledWith(4)
            expect(consoleMock).toHaveBeenCalledWith('buzz')
            expect(consoleMock).toHaveBeenCalledWith('fizz')
            expect(consoleMock).toHaveBeenCalledWith(7)
            expect(consoleMock).toHaveBeenCalledWith(8)
            expect(consoleMock).toHaveBeenCalledWith('fizz')
            expect(consoleMock).toHaveBeenCalledWith('buzz')
        })
        '''
        self.fail('Test not implemented, yet.')

    def test_fibonacci(self):
        '''
        test('Fibonacci sequence', () => {
            expect(fibonacci(0)).toBe(0)
            expect(fibonacci(1)).toBe(1)
            expect(fibonacci(2)).toBe(1)
            expect(fibonacci(3)).toBe(2)
            expect(fibonacci(4)).toBe(3)
            expect(fibonacci(5)).toBe(5)
            expect(fibonacci(10)).toBe(55)
            expect(fibonacci(15)).toBe(610)
        })
        '''
        self.fail('Test not implemented, yet.')