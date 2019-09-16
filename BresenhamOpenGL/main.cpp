/*
	Done by: 100565, 101112, 102214
	
*/

#include <iostream>
#include <tuple>
#include <vector>
#include <Windows.h>
#include <GL/glut.h>

using namespace std;

typedef vector<tuple<float, float>> tuplevector;


class Bresenham {
public:
	tuplevector plots;
	float x0 = 0; float y0 = 0; float x1 = 0; float y1 = 0;
	tuplevector algorithm();
	void drawLine();

};


tuplevector Bresenham::algorithm() {
	// Calculate M
	const float dy = (y1 - y0);
	const float dx = (x1 - x0);
	const float M = dy / dx;
	const float two_dy = 2 * dy;
	const float two_dx = 2 * dx;

	if (M < 1) {
		int iteration = 0;
		// Initial decision parameter
		float decision = two_dy - dx;
		// Initialise start points
		float x = x0;
		float y = y0;

		// Initialise vector with start point
		plots.push_back(make_tuple(x0, y0));

		while (iteration < dx) {
			if (decision < 0) {
				x += 1;
				decision += two_dy;
			}
			else if(decision >= 0) {
				x += 1;
				y += 1;
				decision += (two_dy - two_dx);
			}
			plots.push_back(make_tuple(x, y));
			iteration += 1;
		}
	}
	else {
		int iteration = 0;
		// Initial decision parameter
		float decision = two_dx - dy;
		// Initialise start points
		float x = x0;
		float y = y0;
		// Initialise vector with start point
		plots.push_back(make_tuple(x0, y0));

		while (iteration < dy) {
			if (decision < 0) {
				y += 1;
				decision += two_dx;
			}
			else if(decision >= 0) {
				x += 1;
				y += 1;
				decision += (two_dx - two_dy);
			}
			plots.push_back(make_tuple(x, y));
			iteration += 1;
		}
	}

	return plots;
}

void Bresenham::drawLine() {
	glPointSize(5);

	glColor3f(1, 0, 1);
	glBegin(GL_LINES);
	glVertex2f(x0, y0);
	glVertex2f(x1, y1);
	glEnd();

	glColor3f(1, 1, 0);
	glBegin(GL_POINTS);
	for (auto i = plots.begin(); i != plots.end(); ++i) {
		GLfloat x = get<0>(*i);
		GLfloat y = get<1>(*i);
		glVertex2f(x, y);
	}
	glEnd();
	glFlush();
}

Bresenham bresenhams;

void init() {
	//Set plane color (Black and Opaque)
	glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
	// Define cartesian plane bounds
	double cartesianSize = 20.0;
	gluOrtho2D(-cartesianSize, cartesianSize, -cartesianSize, cartesianSize);
}



void render() {
	bresenhams.drawLine();
}

int main(int argc, char** argv) {
	//float x0, y0, x1, y1;

	cout << "--- Bresenham's Line Drawing Algorithm ---\n";
	cout << "Enter x0: ";
	cin >> bresenhams.x0;

	cout << "Enter y0: ";
	cin >> bresenhams.y0;

	cout << "Enter x1: ";
	cin >> bresenhams.x1;

	cout << "Enter y1: ";
	cin >> bresenhams.y1;

	// Call algorithm
	bresenhams.algorithm();
	
	cout << "Points to plot: \n";
	for (auto i = bresenhams.plots.begin(); i != bresenhams.plots.end(); ++i) {
		cout << "(" << get<0>(*i) << ", " << get<1>(*i) << ")" << endl;
	}

	//Opengl setup
	glutInit(&argc, argv); //Initialize glut
	glutInitWindowPosition(50, 50); // Init window position to the top left corner
	glutInitWindowSize(500, 500); // Window initial window height and width
	glutCreateWindow("Bresnham Line"); // Create window with title
	init();
	glutDisplayFunc(render); // Pass function that renders shape
	glutMainLoop(); //Enter event processing loop

	return 0;
}