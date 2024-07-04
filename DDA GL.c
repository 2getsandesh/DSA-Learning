#include <GL/glut.h>
#include <stdlib.h>

// Function to initialize the OpenGL window
void init() {
    // Set the background color to white
    glClearColor(1.0, 1.0, 1.0, 1.0);
    // Set the color for drawing (black)
    glColor3f(0.0, 0.0, 0.0);
    // Set up the orthographic projection
    gluOrtho2D(0.0, 500.0, 0.0, 500.0);
}

// Function to implement the DDA algorithm and draw the line
void DDA(int x1, int y1, int x2, int y2) {
    int dx = x2 - x1;
    int dy = y2 - y1;
    int steps = abs(dx) > abs(dy) ? abs(dx) : abs(dy);
    float xIncrement = dx / (float) steps;
    float yIncrement = dy / (float) steps;
    float x = x1;
    float y = y1;

    glBegin(GL_POINTS);
    for (int i = 0; i <= steps; i++) {
        glVertex2i(x, y);
        x += xIncrement;
        y += yIncrement;
    }
    glEnd();
    glFlush();
}

// Display callback for GLUT
void display() {
    glClear(GL_COLOR_BUFFER_BIT);

    // Draw a line using DDA from (50, 100) to (450, 400)
    DDA(50, 100, 450, 400);

    glFlush();
}

int main(int argc, char** argv) {
    // Initialize GLUT
    glutInit(&argc, argv);
    // Set display mode to single buffer and RGB color
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    // Set the initial window size
    glutInitWindowSize(500, 500);
    // Create the window with a title
    glutCreateWindow("DDA Line Drawing Algorithm");
    // Initialize the OpenGL environment
    init();
    // Set the display callback function
    glutDisplayFunc(display);
    // Enter the GLUT main loop
    glutMainLoop();
    return 0;
}
