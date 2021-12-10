om = 13261
d = 4
m = [1776, 1456, 1152, 896, 640, 416, 224]
k = [0.9614, 1.0691, 1.1784, 1.3988, 1.6124, 1.6671, 1.9798, 2.0542]
b = [992, 800, 640, 384, 192, 160, 32, 0]
temp = [-70.0, -69.9, -69.8, -69.7, -69.6, -69.5, -69.4, -69.3, -69.2, -69.1, -69.0, -68.9, -68.8, -68.7, -68.6, -68.5,
        -68.4, -68.3, -68.2, -68.1, -68.0, -67.9, -67.8, -67.7, -67.6, -67.5, -67.4, -67.3, -67.2, -67.1, -67.0, -66.9,
        -66.8, -66.7, -66.6, -66.5, -66.4, -66.3, -66.2, -66.1, -66.0, -65.9, -65.8, -65.7, -65.6, -65.5, -65.4, -65.3,
        -65.2, -65.1, -65.0, -64.9, -64.8, -64.7, -64.6, -64.5, -64.4, -64.3, -64.2, -64.1, -64.0, -63.9, -63.8, -63.7,
        -63.6, -63.5, -63.4, -63.3, -63.2, -63.1, -63.0, -62.9, -62.8, -62.7, -62.6, -62.5, -62.4, -62.3, -62.2, -62.1,
        -62.0, -61.9, -61.8, -61.7, -61.6, -61.5, -61.4, -61.3, -61.2, -61.1, -61.0, -60.9, -60.8, -60.7, -60.6, -60.5,
        -60.4, -60.3, -60.2, -60.1, -60.0, -59.9, -59.8, -59.7, -59.6, -59.5, -59.4, -59.3, -59.2, -59.1, -59.0, -58.9,
        -58.8, -58.7, -58.6, -58.5, -58.4, -58.3, -58.2, -58.1, -58.0, -57.9, -57.8, -57.7, -57.6, -57.5, -57.4, -57.3,
        -57.2, -57.1, -57.0, -56.9, -56.8, -56.7, -56.6, -56.5, -56.4, -56.3, -56.2, -56.1, -56.0, -55.9, -55.8, -55.7,
        -55.6, -55.5, -55.4, -55.3, -55.2, -55.1, -55.0, -54.9, -54.8, -54.7, -54.6, -54.5, -54.4, -54.3, -54.2, -54.1,
        -54.0, -53.9, -53.8, -53.7, -53.6, -53.5, -53.4, -53.3, -53.2, -53.1, -53.0, -52.9, -52.8, -52.7, -52.6, -52.5,
        -52.4, -52.3, -52.2, -52.1, -52.0, -51.9, -51.8, -51.7, -51.6, -51.5, -51.4, -51.3, -51.2, -51.1, -51.0, -50.9,
        -50.8, -50.7, -50.6, -50.5, -50.4, -50.3, -50.2, -50.1, -50.0, -49.9, -49.8, -49.7, -49.6, -49.5, -49.4, -49.3,
        -49.2, -49.1, -49.0, -48.9, -48.8, -48.7, -48.6, -48.5, -48.4, -48.3, -48.2, -48.1, -48.0, -47.9, -47.8, -47.7,
        -47.6, -47.5, -47.4, -47.3, -47.2, -47.1, -47.0, -46.9, -46.8, -46.7, -46.6, -46.5, -46.4, -46.3, -46.2, -46.1,
        -46.0, -45.9, -45.8, -45.7, -45.6, -45.5, -45.4, -45.3, -45.2, -45.1, -45.0, -44.9, -44.8, -44.7, -44.6, -44.5,
        -44.4, -44.3, -44.2, -44.1, -44.0, -43.9, -43.8, -43.7, -43.6, -43.5, -43.4, -43.3, -43.2, -43.1, -43.0, -42.9,
        -42.8, -42.7, -42.6, -42.5, -42.4, -42.3, -42.2, -42.1, -42.0, -41.9, -41.8, -41.7, -41.6, -41.5, -41.4, -41.3,
        -41.2, -41.1, -41.0, -40.9, -40.8, -40.7, -40.6, -40.5, -40.4, -40.3, -40.2, -40.1, -40.0, -39.9, -39.8, -39.7,
        -39.6, -39.5, -39.4, -39.3, -39.2, -39.1, -39.0, -38.9, -38.8, -38.7, -38.6, -38.5, -38.4, -38.3, -38.2, -38.1,
        -38.0, -37.9, -37.8, -37.7, -37.6, -37.5, -37.4, -37.3, -37.2, -37.1, -37.0, -36.9, -36.8, -36.7, -36.6, -36.5,
        -36.4, -36.3, -36.2, -36.1, -36.0, -35.9, -35.8, -35.7, -35.6, -35.5, -35.4, -35.3, -35.2, -35.1, -35.0, -34.9,
        -34.8, -34.7, -34.6, -34.5, -34.4, -34.3, -34.2, -34.1, -34.0, -33.9, -33.8, -33.7, -33.6, -33.5, -33.4, -33.3,
        -33.2, -33.1, -33.0, -32.9, -32.8, -32.7, -32.6, -32.5, -32.4, -32.3, -32.2, -32.1, -32.0, -31.9, -31.8, -31.7,
        -31.6, -31.5, -31.4, -31.3, -31.2, -31.1, -31.0, -30.9, -30.8, -30.7, -30.6, -30.5, -30.4, -30.3, -30.2, -30.1,
        -30.0, -29.9, -29.8, -29.7, -29.6, -29.5, -29.4, -29.3, -29.2, -29.1, -29.0, -28.9, -28.8, -28.7, -28.6, -28.5,
        -28.4, -28.3, -28.2, -28.1, -28.0, -27.9, -27.8, -27.7, -27.6, -27.5, -27.4, -27.3, -27.2, -27.1, -27.0, -26.9,
        -26.8, -26.7, -26.6, -26.5, -26.4, -26.3, -26.2, -26.1, -26.0, -25.9, -25.8, -25.7, -25.6, -25.5, -25.4, -25.3,
        -25.2, -25.1, -25.0, -24.9, -24.8, -24.7, -24.6, -24.5, -24.4, -24.3, -24.2, -24.1, -24.0, -23.9, -23.8, -23.7,
        -23.6, -23.5, -23.4, -23.3, -23.2, -23.1, -23.0, -22.9, -22.8, -22.7, -22.6, -22.5, -22.4, -22.3, -22.2, -22.1,
        -22.0, -21.9, -21.8, -21.7, -21.6, -21.5, -21.4, -21.3, -21.2, -21.1, -21.0, -20.9, -20.8, -20.7, -20.6, -20.5,
        -20.4, -20.3, -20.2, -20.1, -20.0, -19.9, -19.8, -19.7, -19.6, -19.5, -19.4, -19.3, -19.2, -19.1, -19.0, -18.9,
        -18.8, -18.7, -18.6, -18.5, -18.4, -18.3, -18.2, -18.1, -18.0, -17.9, -17.8, -17.7, -17.6, -17.5, -17.4, -17.3,
        -17.2, -17.1, -17.0, -16.9, -16.8, -16.7, -16.6, -16.5, -16.4, -16.3, -16.2, -16.1, -16.0, -15.9, -15.8, -15.7,
        -15.6, -15.5, -15.4, -15.3, -15.2, -15.1, -15.0, -14.9, -14.8, -14.7, -14.6, -14.5, -14.4, -14.3, -14.2, -14.1,
        -14.0, -13.9, -13.8, -13.7, -13.6, -13.5, -13.4, -13.3, -13.2, -13.1, -13.0, -12.9, -12.8, -12.7, -12.6, -12.5,
        -12.4, -12.3, -12.2, -12.1, -12.0, -11.9, -11.8, -11.7, -11.6, -11.5, -11.4, -11.3, -11.2, -11.1, -11.0, -10.9,
        -10.8, -10.7, -10.6, -10.5, -10.4, -10.3, -10.2, -10.1, -10.0, -9.9, -9.8, -9.7, -9.6, -9.5, -9.4, -9.3, -9.2,
        -9.1, -9.0, -8.9, -8.8, -8.7, -8.6, -8.5, -8.4, -8.3, -8.2, -8.1, -8.0, -7.9, -7.8, -7.7, -7.6, -7.5, -7.4,
        -7.3, -7.2, -7.1, -7.0, -6.9, -6.8, -6.7, -6.6, -6.5, -6.4, -6.3, -6.2, -6.1, -6.0, -5.9, -5.8, -5.7, -5.6,
        -5.5, -5.4, -5.3, -5.2, -5.1, -5.0, -4.9, -4.8, -4.7, -4.6, -4.5, -4.4, -4.3, -4.2, -4.1, -4.0, -3.9, -3.8,
        -3.7, -3.6, -3.5, -3.4, -3.3, -3.2, -3.1, -3.0, -2.9, -2.8, -2.7, -2.6, -2.5, -2.4, -2.3, -2.2, -2.1, -2.0,
        -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2,
        -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0,
        2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2,
        4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4,
        6.5, 6.6, 6.7, 6.8, 6.9, 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.0, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6,
        8.7, 8.8, 8.9, 9.0, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10.0, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7,
        10.8, 10.9, 11.0, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 12.0, 12.1, 12.2, 12.3, 12.4, 12.5,
        12.6, 12.7, 12.8, 12.9, 13.0, 13.1, 13.2, 13.3, 13.4, 13.5, 13.6, 13.7, 13.8, 13.9, 14.0, 14.1, 14.2, 14.3,
        14.4, 14.5, 14.6, 14.7, 14.8, 14.9, 15.0, 15.1, 15.2, 15.3, 15.4, 15.5, 15.6, 15.7, 15.8, 15.9, 16.0, 16.1,
        16.2, 16.3, 16.4, 16.5, 16.6, 16.7, 16.8, 16.9, 17.0, 17.1, 17.2, 17.3, 17.4, 17.5, 17.6, 17.7, 17.8, 17.9,
        18.0, 18.1, 18.2, 18.3, 18.4, 18.5, 18.6, 18.7, 18.8, 18.9, 19.0, 19.1, 19.2, 19.3, 19.4, 19.5, 19.6, 19.7,
        19.8, 19.9, 20.0, 20.1, 20.2, 20.3, 20.4, 20.5, 20.6, 20.7, 20.8, 20.9, 21.0, 21.1, 21.2, 21.3, 21.4, 21.5,
        21.6, 21.7, 21.8, 21.9, 22.0, 22.1, 22.2, 22.3, 22.4, 22.5, 22.6, 22.7, 22.8, 22.9, 23.0, 23.1, 23.2, 23.3,
        23.4, 23.5, 23.6, 23.7, 23.8, 23.9, 24.0, 24.1, 24.2, 24.3, 24.4, 24.5, 24.6, 24.7, 24.8, 24.9, 25.0, 25.1,
        25.2, 25.3, 25.4, 25.5, 25.6, 25.7, 25.8, 25.9, 26.0, 26.1, 26.2, 26.3, 26.4, 26.5, 26.6, 26.7, 26.8, 26.9,
        27.0, 27.1, 27.2, 27.3, 27.4, 27.5, 27.6, 27.7, 27.8, 27.9, 28.0, 28.1, 28.2, 28.3, 28.4, 28.5, 28.6, 28.7,
        28.8, 28.9, 29.0, 29.1, 29.2, 29.3, 29.4, 29.5, 29.6, 29.7, 29.8, 29.9, 30.0, 30.1, 30.2, 30.3, 30.4, 30.5,
        30.6, 30.7, 30.8, 30.9, 31.0, 31.1, 31.2, 31.3, 31.4, 31.5, 31.6, 31.7, 31.8, 31.9, 32.0, 32.1, 32.2, 32.3,
        32.4, 32.5, 32.6, 32.7, 32.8, 32.9, 33.0, 33.1, 33.2, 33.3, 33.4, 33.5, 33.6, 33.7, 33.8, 33.9, 34.0, 34.1,
        34.2, 34.3, 34.4, 34.5, 34.6, 34.7, 34.8, 34.9, 35.0, 35.1, 35.2, 35.3, 35.4, 35.5, 35.6, 35.7, 35.8, 35.9,
        36.0, 36.1, 36.2, 36.3, 36.4, 36.5, 36.6, 36.7, 36.8, 36.9, 37.0, 37.1, 37.2, 37.3, 37.4, 37.5, 37.6, 37.7,
        37.8, 37.9, 38.0, 38.1, 38.2, 38.3, 38.4, 38.5, 38.6, 38.7, 38.8, 38.9, 39.0, 39.1, 39.2, 39.3, 39.4, 39.5,
        39.6, 39.7, 39.8, 39.9, 40.0, 40.1, 40.2, 40.3, 40.4, 40.5, 40.6, 40.7, 40.8, 40.9, 41.0, 41.1, 41.2, 41.3,
        41.4, 41.5, 41.6, 41.7, 41.8, 41.9, 42.0, 42.1, 42.2, 42.3, 42.4, 42.5, 42.6, 42.7, 42.8, 42.9, 43.0, 43.1,
        43.2, 43.3, 43.4, 43.5, 43.6, 43.7, 43.8, 43.9, 44.0, 44.1, 44.2, 44.3, 44.4, 44.5, 44.6, 44.7, 44.8, 44.9,
        45.0, 45.1, 45.2, 45.3, 45.4, 45.5, 45.6, 45.7, 45.8, 45.9, 46.0, 46.1, 46.2, 46.3, 46.4, 46.5, 46.6, 46.7,
        46.8, 46.9, 47.0, 47.1, 47.2, 47.3, 47.4, 47.5, 47.6, 47.7, 47.8, 47.9, 48.0, 48.1, 48.2, 48.3, 48.4, 48.5,
        48.6, 48.7, 48.8, 48.9, 49.0, 49.1, 49.2, 49.3, 49.4, 49.5, 49.6, 49.7, 49.8, 49.9, 50.0, 50.1, 50.2, 50.3,
        50.4, 50.5, 50.6, 50.7, 50.8, 50.9, 51.0, 51.1, 51.2, 51.3, 51.4, 51.5, 51.6, 51.7, 51.8, 51.9, 52.0, 52.1,
        52.2, 52.3, 52.4, 52.5, 52.6, 52.7, 52.8, 52.9, 53.0, 53.1, 53.2, 53.3, 53.4, 53.5, 53.6, 53.7, 53.8, 53.9,
        54.0, 54.1, 54.2, 54.3, 54.4, 54.5, 54.6, 54.7, 54.8, 54.9, 55.0, 55.1, 55.2, 55.3, 55.4, 55.5, 55.6, 55.7,
        55.8, 55.9, 56.0, 56.1, 56.2, 56.3, 56.4, 56.5, 56.6, 56.7, 56.8, 56.9, 57.0, 57.1, 57.2, 57.3, 57.4, 57.5,
        57.6, 57.7, 57.8, 57.9, 58.0, 58.1, 58.2, 58.3, 58.4, 58.5, 58.6, 58.7, 58.8, 58.9, 59.0, 59.1, 59.2, 59.3,
        59.4, 59.5, 59.6, 59.7, 59.8, 59.9, 60.0, 60.1, 60.2, 60.3, 60.4, 60.5, 60.6, 60.7, 60.8, 60.9, 61.0, 61.1,
        61.2, 61.3, 61.4, 61.5, 61.6, 61.7, 61.8, 61.9, 62.0, 62.1, 62.2, 62.3, 62.4, 62.5, 62.6, 62.7, 62.8, 62.9,
        63.0, 63.1, 63.2, 63.3, 63.4, 63.5, 63.6, 63.7, 63.8, 63.9, 64.0, 64.1, 64.2, 64.3, 64.4, 64.5, 64.6, 64.7,
        64.8, 64.9, 65.0, 65.1, 65.2, 65.3, 65.4, 65.5, 65.6, 65.7, 65.8, 65.9, 66.0, 66.1, 66.2, 66.3, 66.4, 66.5,
        66.6, 66.7, 66.8, 66.9, 67.0, 67.1, 67.2, 67.3, 67.4, 67.5, 67.6, 67.7, 67.8, 67.9, 68.0, 68.1, 68.2, 68.3,
        68.4, 68.5, 68.6, 68.7, 68.8, 68.9, 69.0, 69.1, 69.2, 69.3, 69.4, 69.5, 69.6, 69.7, 69.8, 69.9, 70.0, 70.1,
        70.2, 70.3, 70.4, 70.5, 70.6, 70.7, 70.8, 70.9, 71.0, 71.1, 71.2, 71.3, 71.4, 71.6, 71.7, 71.8, 71.9, 72.0,
        72.1, 72.2, 72.3, 72.4, 72.5, 72.6, 72.7, 72.8, 72.9, 73.0, 73.1, 73.2, 73.3, 73.4, 73.5, 73.6, 73.7, 73.8,
        73.9, 74.0, 74.1, 74.2, 74.3, 74.4, 74.5, 74.6, 74.7, 74.8, 74.9, 75.0, 75.1, 75.2, 75.3, 75.4, 75.5, 75.6,
        75.7, 75.8, 75.9, 76.0, 76.1, 76.2, 76.3, 76.4, 76.5, 76.6, 76.7, 76.8, 76.9, 77.0, 77.1, 77.2, 77.3, 77.4,
        77.5, 77.6, 77.7, 77.8, 77.9, 78.0, 78.1, 78.2, 78.3, 78.4, 78.5, 78.6, 78.7, 78.8, 78.9, 79.0, 79.1, 79.2,
        79.3, 79.4, 79.5, 79.6, 79.7, 79.8, 79.9, 80.0, 80.1, 80.2, 80.3, 80.4, 80.5, 80.6, 80.7, 80.8, 80.9, 81.0,
        81.1, 81.2, 81.3, 81.4, 81.5, 81.6, 81.7, 81.8, 81.9, 82.0, 82.1, 82.2, 82.3, 82.4, 82.5, 82.6, 82.7, 82.8,
        82.9, 83.0, 83.1, 83.2, 83.3, 83.4, 83.5, 83.6, 83.7, 83.8, 83.9, 84.0, 84.1, 84.2, 84.3, 84.4, 84.5, 84.6,
        84.7, 84.8, 84.9, 85.0, 85.1, 85.2, 85.3, 85.4, 85.5, 85.6, 85.7, 85.8, 85.9, 86.0, 86.1, 86.2, 86.3, 86.4,
        86.5, 86.6, 86.7, 86.8, 86.9, 87.0, 87.1, 87.2, 87.3, 87.4, 87.5, 87.6, 87.7, 87.8, 87.9, 88.0, 88.1, 88.2,
        88.3, 88.4, 88.5, 88.6, 88.7, 88.8, 88.9, 89.0, 89.1, 89.2, 89.3, 89.4, 89.5, 89.6, 89.7, 89.8, 89.9, 90.0,
        90.1, 90.2, 90.3, 90.4, 90.5, 90.6, 90.7, 90.8, 90.9, 91.0, 91.1, 91.2, 91.3, 91.4, 91.5, 91.6, 91.7, 91.8,
        91.9, 92.0, 92.1, 92.2, 92.3, 92.4, 92.5, 92.6, 92.7, 92.8, 92.9, 93.0, 93.1, 93.2, 93.3, 93.4, 93.5, 93.6,
        93.7, 93.8, 93.9, 94.0, 94.1, 94.2, 94.3, 94.4, 94.5, 94.6, 94.7, 94.8, 94.9, 95.0, 95.1, 95.2, 95.3, 95.4,
        95.5, 95.6, 95.7, 95.8, 95.9, 96.0, 96.1, 96.2, 96.3, 96.4, 96.5, 96.6, 96.7, 96.8, 96.9, 97.0, 97.1, 97.2,
        97.3, 97.4, 97.5, 97.6, 97.7, 97.8, 97.9, 98.0, 98.1, 98.2, 98.3, 98.4, 98.5, 98.6, 98.7, 98.8, 98.9, 99.0,
        99.1, 99.2, 99.3, 99.4, 99.5, 99.6, 99.7, 99.8, 99.9, 100.0, 100.1, 100.2, 100.3, 100.4, 100.5, 100.6, 100.7,
        100.8, 100.9, 101.0, 101.1, 101.2, 101.3, 101.4, 101.5, 101.6, 101.7, 101.8, 101.9, 102.0, 102.1, 102.2, 102.3,
        102.4, 102.5, 102.6, 102.7, 102.8, 102.9, 103.0, 103.1, 103.2, 103.3, 103.4, 103.5, 103.6, 103.7, 103.8, 103.9,
        104.0, 104.1, 104.2, 104.3, 104.4, 104.5, 104.6, 104.7, 104.8, 104.9, 105.0, 105.1, 105.2, 105.3, 105.4, 105.5,
        105.6, 105.7, 105.8, 105.9, 106.0, 106.1, 106.2, 106.3, 106.4, 106.5, 106.6, 106.7, 106.8, 106.9, 107.0, 107.1,
        107.2, 107.3, 107.4, 107.5, 107.6, 107.7, 107.8, 107.9, 108.0, 108.1, 108.2, 108.3, 108.4, 108.5, 108.6, 108.7,
        108.8, 108.9, 109.0, 109.1, 109.2, 109.3, 109.4, 109.5, 109.6, 109.7, 109.8, 109.9, 110.0, 110.1, 110.2, 110.3,
        110.4, 110.5, 110.6, 110.7, 110.8, 110.9, 111.0, 111.1, 111.2, 111.3, 111.4, 111.5, 111.6, 111.7, 111.8, 111.9,
        112.0, 112.1, 112.2, 112.3, 112.4, 112.5, 112.6, 112.7, 112.8, 112.9, 113.0, 113.1, 113.2, 113.3, 113.4, 113.5,
        113.6, 113.7, 113.8, 113.9, 114.0, 114.1, 114.2, 114.3, 114.4, 114.5, 114.6, 114.7, 114.8, 114.9, 115.0, 115.1,
        115.2, 115.3, 115.4, 115.5, 115.6, 115.7, 115.8, 115.9, 116.0, 116.1, 116.2, 116.3, 116.4, 116.5, 116.6, 116.7,
        116.8, 116.9, 117.0, 117.1, 117.2, 117.3, 117.4, 117.5, 117.6, 117.7, 117.8, 117.9, 118.0, 118.1, 118.2, 118.3,
        118.4, 118.5, 118.6, 118.7, 118.8, 118.9, 119.0, 119.1, 119.2, 119.3, 119.4, 119.5, 119.6, 119.7, 119.8, 119.9,
        120.0, 120.1, 120.2, 120.3, 120.4, 120.5, 120.6, 120.7, 120.8, 120.9, 121.0, 121.1, 121.2, 121.3, 121.4, 121.5,
        121.6, 121.7, 121.8, 121.9, 122.0, 122.1, 122.2, 122.3, 122.4, 122.5, 122.6, 122.7, 122.8, 122.9, 123.0, 123.1,
        123.2, 123.3, 123.4, 123.5, 123.6, 123.7, 123.8, 123.9, 124.0, 124.1, 124.2, 124.3, 124.4, 124.5, 124.6, 124.7,
        124.8, 124.9, 125.0, 125.1, 125.2, 125.3, 125.4, 125.5, 125.6, 125.7, 125.8, 125.9, 126.0, 126.1, 126.2, 126.3,
        126.4, 126.5, 126.6, 126.7, 126.8, 126.9, 127.0, 127.1, 127.2, 127.3, 127.4, 127.5, 127.6, 127.7, 127.8, 127.9,
        128.0, 128.1, 128.2, 128.3, 128.4, 128.5, 128.6, 128.7, 128.8, 128.9, 129.0, 129.1, 129.2, 129.3, 129.4, 129.5,
        129.6, 129.7, 129.8, 129.9, ]
cod = [22401, 22397, 22389, 22381, 22374, 22366, 22358, 22351, 22343, 22335, 22328, 22284, 22277, 22269, 22262, 22258,
       22250, 22242, 22235, 22227, 22224, 22217, 22209, 22201, 22194, 22186, 22179, 22171, 22164, 22156, 22149, 22141,
       22133, 22126, 22118, 22113, 22106, 22098, 22096, 22089, 22081, 22074, 22066, 22059, 22051, 22044, 22037, 22029,
       22022, 22014, 22007, 21999, 21992, 21984, 21978, 21971, 21970, 21963, 21955, 21948, 21941, 21933, 21926, 21918,
       21911, 21904, 21896, 21889, 21882, 21874, 21867, 21859, 21852, 21845, 21845, 21838, 21831, 21823, 21816, 21809,
       21801, 21794, 21787, 21780, 21772, 21765, 21758, 21750, 21743, 21736, 21729, 21721, 21687, 21680, 21672, 21665,
       21658, 21651, 21644, 21636, 21629, 21622, 21615, 21608, 21600, 21593, 21586, 21579, 21572, 21572, 21565, 21558,
       21551, 21544, 21536, 21529, 21522, 21515, 21508, 21501, 21494, 21487, 21479, 21472, 21465, 21461, 21454, 21452,
       21444, 21437, 21430, 21423, 21416, 21409, 21402, 21395, 21388, 21381, 21374, 21367, 21360, 21353, 21349, 21342,
       21336, 21332, 21325, 21318, 21311, 21304, 21297, 21290, 21283, 21276, 21269, 21262, 21255, 21249, 21246, 21239,
       21232, 21225, 21221, 21214, 21207, 21200, 21194, 21187, 21180, 21173, 21166, 21125, 21118, 21111, 21110, 21103,
       21096, 21089, 21082, 21077, 21070, 21063, 21057, 21050, 21043, 21036, 21029, 21022, 21016, 21009, 21002, 21001,
       20995, 20988, 20981, 20974, 20969, 20962, 20955, 20948, 20941, 20935, 20928, 20921, 20914, 20908, 20901, 20901,
       20894, 20888, 20881, 20874, 20868, 20861, 20854, 20848, 20841, 20835, 20828, 20821, 20815, 20808, 20801, 20801,
       20795, 20788, 20781, 20775, 20768, 20761, 20755, 20748, 20742, 20736, 20729, 20723, 20716, 20709, 20703, 20702,
       20695, 20689, 20682, 20676, 20669, 20662, 20656, 20618, 20611, 20605, 20598, 20592, 20585, 20579, 20572, 20570,
       20564, 20557, 20551, 20544, 20538, 20531, 20527, 20521, 20514, 20508, 20501, 20495, 20489, 20482, 20476, 20473,
       20467, 20460, 20454, 20447, 20441, 20438, 20431, 20425, 20418, 20412, 20406, 20399, 20393, 20386, 20383, 20377,
       20370, 20364, 20357, 20351, 20349, 20342, 20336, 20330, 20323, 20317, 20311, 20304, 20298, 20292, 20288, 20281,
       20275, 20269, 20262, 20261, 20254, 20248, 20242, 20235, 20229, 20223, 20217, 20210, 20204, 20198, 20193, 20187,
       20181, 20174, 20141, 20134, 20128, 20122, 20116, 20109, 20103, 20097, 20091, 20085, 20078, 20073, 20067, 20060,
       20060, 20054, 20048, 20042, 20036, 20029, 20023, 20017, 20011, 20005, 19999, 19992, 19986, 19980, 19974, 19974,
       19968, 19962, 19956, 19950, 19944, 19938, 19932, 19925, 19919, 19913, 19907, 19901, 19895, 19895, 19888, 19883,
       19877, 19871, 19865, 19859, 19853, 19847, 19841, 19835, 19829, 19823, 19817, 19811, 19810, 19805, 19799, 19793,
       19787, 19781, 19775, 19769, 19763, 19757, 19751, 19745, 19739, 19733, 19701, 19695, 19689, 19683, 19677, 19671,
       19665, 19659, 19653, 19647, 19642, 19636, 19630, 19624, 19621, 19618, 19612, 19606, 19600, 19595, 19589, 19583,
       19577, 19571, 19565, 19559, 19553, 19547, 19545, 19542, 19536, 19530, 19524, 19518, 19512, 19507, 19501, 19495,
       19489, 19483, 19477, 19476, 19470, 19466, 19460, 19454, 19449, 19443, 19437, 19431, 19425, 19419, 19414, 19408,
       19402, 19401, 19395, 19391, 19385, 19379, 19373, 19368, 19362, 19356, 19350, 19345, 19339, 19333, 19332, 19327,
       19321, 19285, 19279, 19273, 19267, 19262, 19256, 19250, 19245, 19239, 19233, 19233, 19228, 19222, 19216, 19211,
       19205, 19199, 19194, 19188, 19182, 19177, 19171, 19166, 19166, 19160, 19154, 19149, 19143, 19137, 19132, 19126,
       19120, 19115, 19110, 19104, 19099, 19093, 19093, 19087, 19081, 19076, 19070, 19064, 19059, 19054, 19049, 19043,
       19038, 19032, 19027, 19026, 19020, 19014, 19009, 19003, 18998, 18992, 18988, 18983, 18977, 18972, 18966, 18961,
       18959, 18954, 18948, 18943, 18937, 18931, 18897, 18892, 18886, 18881, 18875, 18870, 18864, 18862, 18857, 18851,
       18846, 18840, 18835, 18832, 18827, 18821, 18816, 18810, 18805, 18799, 18797, 18791, 18786, 18780, 18775, 18773,
       18767, 18762, 18756, 18751, 18746, 18740, 18735, 18732, 18726, 18721, 18715, 18710, 18708, 18703, 18698, 18692,
       18687, 18682, 18676, 18671, 18667, 18662, 18656, 18651, 18650, 18644, 18639, 18634, 18628, 18623, 18618, 18613,
       18607, 18603, 18598, 18592, 18592, 18586, 18581, 18576, 18570, 18565, 18530, 18524, 18519, 18514, 18509, 18503,
       18503, 18498, 18493, 18488, 18482, 18477, 18472, 18467, 18461, 18456, 18451, 18446, 18441, 18441, 18435, 18430,
       18425, 18420, 18415, 18410, 18404, 18399, 18394, 18389, 18384, 18383, 18379, 18373, 18368, 18363, 18358, 18353,
       18348, 18342, 18337, 18332, 18327, 18326, 18322, 18317, 18312, 18307, 18301, 18296, 18291, 18286, 18281, 18276,
       18271, 18271, 18266, 18261, 18255, 18250, 18245, 18240, 18235, 18230, 18225, 18220, 18215, 18185, 18180, 18175,
       18170, 18165, 18160, 18154, 18149, 18144, 18139, 18134, 18132, 18129, 18124, 18119, 18114, 18109, 18104, 18099,
       18094, 18089, 18084, 18079, 18077, 18074, 18069, 18064, 18059, 18054, 18049, 18044, 18039, 18034, 18029, 18027,
       18024, 18019, 18014, 18009, 18004, 17999, 17994, 17989, 17984, 17979, 17978, 17973, 17970, 17965, 17960, 17955,
       17950, 17945, 17940, 17935, 17930, 17925, 17924, 17919, 17915, 17910, 17906, 17901, 17896, 17891, 17856, 17851,
       17847, 17846, 17841, 17836, 17832, 17827, 17822, 17817, 17812, 17808, 17803, 17798, 17798, 17793, 17788, 17783,
       17778, 17774, 17769, 17764, 17759, 17754, 17750, 17750, 17745, 17740, 17735, 17730, 17725, 17720, 17716, 17711,
       17706, 17702, 17701, 17696, 17692, 17687, 17682, 17677, 17672, 17668, 17664, 17659, 17654, 17653, 17649, 17644,
       17639, 17634, 17629, 17626, 17621, 17616, 17611, 17607, 17606, 17601, 17596, 17591, 17587, 17582, 17550, 17545,
       17540, 17536, 17531, 17529, 17524, 17520, 17515, 17510, 17508, 17503, 17498, 17493, 17489, 17484, 17482, 17477,
       17473, 17468, 17463, 17461, 17456, 17452, 17447, 17442, 17438, 17435, 17430, 17426, 17421, 17419, 17414, 17410,
       17405, 17401, 17396, 17391, 17389, 17384, 17379, 17375, 17373, 17368, 17364, 17359, 17354, 17350, 17345, 17342,
       17338, 17333, 17332, 17327, 17322, 17318, 17313, 17309, 17304, 17299, 17296, 17291, 17262, 17257, 17253, 17248,
       17244, 17239, 17235, 17230, 17226, 17222, 17217, 17217, 17212, 17207, 17203, 17198, 17194, 17189, 17185, 17181,
       17176, 17176, 17171, 17167, 17162, 17158, 17153, 17149, 17144, 17140, 17135, 17135, 17131, 17126, 17122, 17117,
       17113, 17108, 17104, 17099, 17095, 17090, 17091, 17086, 17082, 17077, 17073, 17068, 17064, 17059, 17055, 17050,
       17051, 17046, 17042, 17037, 17033, 17028, 17024, 17019, 17015, 17010, 16983, 16978, 16974, 16969, 16965, 16960,
       16956, 16952, 16947, 16943, 16943, 16939, 16934, 16930, 16925, 16921, 16916, 16912, 16908, 16905, 16903, 16899,
       16895, 16890, 16886, 16881, 16877, 16873, 16868, 16866, 16864, 16860, 16855, 16851, 16847, 16842, 16838, 16834,
       16829, 16827, 16825, 16821, 16816, 16812, 16808, 16803, 16799, 16795, 16793, 16789, 16786, 16782, 16777, 16773,
       16769, 16764, 16760, 16756, 16754, 16750, 16746, 16715, 16711, 16707, 16702, 16698, 16694, 16690, 16689, 16684,
       16681, 16677, 16673, 16668, 16664, 16660, 16655, 16655, 16651, 16646, 16643, 16638, 16634, 16630, 16626, 16621,
       16617, 16617, 16613, 16608, 16605, 16600, 16596, 16592, 16588, 16583, 16583, 16579, 16575, 16571, 16567, 16562,
       16558, 16554, 16550, 16545, 16546, 16541, 16537, 16533, 16529, 16525, 16521, 16516, 16512, 16512, 16508, 16504,
       16499, 16495, 16464, 16460, 16456, 16452, 16448, 16447, 16443, 16439, 16435, 16431, 16427, 16423, 16419, 16415,
       16414, 16410, 16406, 16401, 16398, 16394, 16390, 16386, 16382, 16381, 16377, 16373, 16368, 16366, 16362, 16358,
       16353, 16349, 16345, 16344, 16340, 16336, 16333, 16329, 16325, 16321, 16317, 16313, 16311, 16307, 16303, 16301,
       16297, 16292, 16288, 16284, 16280, 16278, 16274, 16270, 16268, 16264, 16260, 16256, 16252, 16221, 16217, 16215,
       16211, 16209, 16205, 16201, 16197, 16193, 16189, 16185, 16182, 16178, 16177, 16173, 16169, 16165, 16161, 16157,
       16153, 16150, 16146, 16145, 16141, 16137, 16133, 16129, 16125, 16121, 16118, 16114, 16113, 16109, 16105, 16101,
       16097, 16093, 16089, 16085, 16086, 16082, 16078, 16074, 16070, 16066, 16062, 16058, 16054, 16054, 16050, 16046,
       16042, 16038, 16034, 16030, 16026, 16022, 15996, 15992, 15988, 15984, 15980, 15976, 15972, 15969, 15965, 15965,
       15961, 15957, 15953, 15949, 15945, 15941, 15937, 15934, 15934, 15930, 15926, 15922, 15918, 15914, 15910, 15907,
       15906, 15903, 15899, 15895, 15891, 15887, 15883, 15879, 15876, 15875, 15872, 15868, 15864, 15860, 15856, 15852,
       15849, 15846, 15845, 15841, 15837, 15833, 15829, 15825, 15823, 15819, 15815, 15814, 15810, 15806, 15802, 15772,
       15769, 15766, 15763, 15761, 15757, 15753, 15749, 15746, 15742, 15740, 15736, 15732, 15731, 15727, 15723, 15719,
       15715, 15711, 15710, 15706, 15704, 15700, 15696, 15693, 15689, 15685, 15684, 15680, 15676, 15674, 15670, 15666,
       15662, 15659, 15657, 15654, 15650, 15646, 15644, 15640, 15636, 15632, 15631, 15628, 15624, 15620, 15617, 15614,
       15610, 15606, 15602, 15602, 15598, 15594, 15590, 15562, 15558, 15554, 15550, 15550, 15546, 15543, 15539, 15536,
       15532, 15528, 15524, 15524, 15520, 15517, 15513, 15509, 15506, 15502, 15498, 15498, 15495, 15491, 15487, 15484,
       15480, 15476, 15473, 15473, 15469, 15465, 15462, 15458, 15455, 15451, 15447, 15444, 15443, 15440, 15436, 15433,
       15429, 15425, 15422, 15418, 15418, 15414, 15411, 15407, 15404, 15400, 15396, 15393, 15392, 15388, 15360, 15357,
       15353, 15349, 15346, 15342, 15341, 15337, 15335, 15331, 15328, 15324, 15321, 15317, 15316, 15313, 15310, 15306,
       15303, 15299, 15295, 15292, 15290, 15288, 15285, 15281, 15278, 15274, 15270, 15267, 15265, 15263, 15260, 15256,
       15253, 15249, 15245, 15242, 15240, 15238, 15235, 15231, 15228, 15224, 15221, 15217, 15217, 15214, 15210, 15207,
       15203, 15199, 15196, 15192, 15167, 15164, 15160, 15157, 15153, 15150, 15146, 15143, 15143, 15139, 15136, 15132,
       15129, 15125, 15122, 15118, 15118, 15115, 15111, 15108, 15104, 15101, 15097, 15096, 15094, 15090, 15087, 15083,
       15080, 15076, 15073, 15072, 15069, 15066, 15062, 15055, 15052, 15048, 15048, 15045, 15041, 15038, 15034, 15031,
       15027, 15027, 15024, 15021, 15017, 15014, 15010, 15007, 15003, 14979, 14975, 14972, 14968, 14965, 14962, 14958,
       14958, 14954, 14951, 14948, 14944, 14941, 14938, 14934, 14934, 14930, 14927, 14924, 14920, 14917, 14914, 14913,
       14910, 14906, 14903, 14900, 14897, 14894, 14890, 14889, 14886, 14883, 14879, 14876, 14873, 14870, 14869, 14866,
       14862, 14859, 14855, 14853, 14850, 14846, 14845, 14842, 14838, 14835, 14833, 14830, 14826, 14823, 14797, 14794,
       14790, 14788, 14785, 14782, 14778, 14777, 14773, 14770, 14768, 14765, 14762, 14758, 14755, 14753, 14750, 14747,
       14745, 14742, 14739, 14735, 14733, 14730, 14727, 14725, 14722, 14719, 14715, 14712, 14710, 14707, 14705, 14702,
       14699, 14695, 14692, 14690, 14687, 14686, 14682, 14679, 14676, 14672, 14670, 14667, 14666, 14663, 14659, 14656,
       14653, 14649, 14623, 14619, 14619, 14616, 14612, 14609, 14606, 14603, 14600, 14599, 14596, 14593, 14589, 14586,
       14583, 14580, 14580, 14576, 14573, 14570, 14567, 14563, 14560, 14560, 14557, 14554, 14550, 14547, 14544, 14541,
       14541, 14537, 14534, 14531, 14528, 14524, 14521, 14521, 14518, 14515, 14512, 14508, 14505, 14502, 14502, 14499,
       14495, 14492, 14489, 14486, 14483, 14459, 14456, 14452, 14449, 14446, 14443, 14439, 14437, 14436, 14433, 14430,
       14427, 14423, 14420, 14418, 14417, 14414, 14411, 14408, 14404, 14401, 14399, 14398, 14395, 14392, 14388, 14385,
       14382, 14380, 14379, 14376, 14373, 14369, 14366, 14364, 14361, 14360, 14357, 14354, 14350, 14347, 14346, 14342,
       14341, 14338, 14335, 14332, 14328, 14327, 14324, 14322, 14295, 14292, 14289, 14286, 14285, 14281, 14280, 14276,
       14273, 14270, 14269, 14266, 14264, 14261, 14258, 14255, 14251, 14250, 14247, 14244, 14242, 14239, 14236, 14233,
       14232, 14229, 14226, 14223, 14220, 14217, 14214, 14213, 14210, 14208, 14205, 14202, 14199, 14198, 14195, 14192,
       14189, 14186, 14183, 14180, 14180, 14176, 14173, 14171, 14168, 14164, 14161, 14138, 14135, 14132, 14129, 14126,
       14123, 14123, 14119, 14116, 14113, 14110, 14107, 14104, 14104, 14101, 14098, 14095, 14092, 14089, 14086, 14086,
       14083, 14080, 14077, 14074, 14071, 14071, 14068, 14064, 14062, 14059, 14056, 14053, 14052, 14049, 14047, 14044,
       14041, 14038, 14037, 14034, 14031, 14029, 14026, 14023, 14020, 14019, 14016, 14014, 13988, 13985, 13982, 13979,
       13978, 13976, 13973, 13970, 13967, 13964, 13962, 13959, 13958, 13955, 13952, 13949, 13946, 13944, 13943, 13940,
       13937, 13934, 13931, 13929, 13928, 13925, 13922, 13919, 13916, 13913, 13911, 13910, 13907, 13904, 13901, 13898,
       13897, 13895, 13892, 13889, 13886, 13883, 13880, 13880, 13877, 13875, 13872, 13869, 13866, 13863, 13840, 13837,
       13834, 13831, 13828, 13825, 13825, 13822, 13819, 13816, 13813, 13811, 13810, 13808, 13805, 13802, 13799, 13796,
       13795, 13793, 13790, 13787, 13784, 13781, 13778, 13778, 13775, 13773, 13770, 13767, 13764, 13763, 13761, 13758,
       13755, 13752, 13749, 13749, 13746, 13743, 13741, 13738, 13735, 13732, 13732, 13729, 13726, 13723, 13698, 13695,
       13695, 13692, 13689, 13686, 13683, 13681, 13680, 13677, 13675, 13672, 13669, 13666, 13666, 13663, 13660, 13657,
       13655, 13652, 13649, 13649, 13646, 13643, 13641, 13638, 13635, 13634, 13632, 13629, 13627, 13624, 13621, 13620,
       13617, 13614, 13612, 13609, 13607, 13606, 13603, 13600, 13598, 13595, 13593, 13592, 13589, 13586, 13562, 13559,
       13556, 13555, 13552, 13549, 13548, 13545, 13542, 13539, 13538, 13535, 13534, 13531, 13528, 13525, 13524, 13521,
       13520, 13517, 13514, 13511, 13510, 13507, 13506, 13503, 13500, 13497, 13496, 13493, 13492, 13489, 13486, 13483,
       13482, 13479, 13478, 13475, 13472, 13469, 13468, 13465, 13464, 13461, 13458, 13456, 13454, 13451, 13428, 13425,
       13422, 13420, 13418, 13415, 13414, 13411, 13409, 13406, 13403, 13401, 13400, 13398, 13395, 13392, 13389, 13387,
       13387, 13384, 13381, 13378, 13376, 13373, 13373, 13370, 13367, 13365, 13362, 13362, 13359, 13356, 13354, 13351,
       13348, 13348, 13345, 13343, 13340, 13337, 13335, 13335, 13332, 13329, 13326, 13324, 13321, 13299, 13296, 13294,
       13291, 13288, 13285, 13285, 13283, 13280, 13277, 13275, 13272, 13272, 13269, 13266, 13264, 13261, 13259, ]
for iterator in range(len(cod)):
    new_cod = (cod[iterator] - om) / d
    new_temp_cod = 0
    if new_cod > m[0]:
        new_temp_cod = new_cod * k[0] + b[0]
    if m[0] > new_cod > m[1]:
        new_temp_cod = new_cod * k[1] + b[1]
    if m[1] > new_cod > m[2]:
        new_temp_cod = new_cod * k[2] + b[2]
    if m[2] > new_cod > m[3]:
        new_temp_cod = new_cod * k[3] + b[3]
    if m[3] > new_cod > m[4]:
        new_temp_cod = new_cod * k[4] + b[4]
    if m[4] > new_cod > m[5]:
        new_temp_cod = new_cod * k[5] + b[5]
    if m[5] > new_cod > m[6]:
        new_temp_cod = new_cod * k[6] + b[6]
    if m[6] > new_cod:
        new_temp_cod = new_cod * k[7] + b[7]
    result = 0
    if new_temp_cod >= 2048:
        result = -1 * (int(new_temp_cod) - 2048) * 0.0625
    else:
        result = (2047 - int(new_temp_cod)) * 0.0625
    if abs(temp[iterator] - result) > 1:
        print(str(temp[iterator] - result) + " __ " + str(temp[iterator]))
