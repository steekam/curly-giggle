/*#include <Windows.h> //Windows
#include <GL/glut.h> //glut library
#include <math.h> //trigonometry function for smoothness

void init() {
	//Set plane color (Black and Opaque)
	glClearColor(0.0f, 0.0f, 0.0f, 1.0f);		
	// Define cartesian plane bounds
	double cartesianSize = 5.0;
	gluOrtho2D(-cartesianSize, cartesianSize, -cartesianSize, cartesianSize);
}

void changeViewPort(int w, int h){
	glViewport(0, 0, w, h);
}

void render() {
	glPointSize(4);

	//Square
	float squareSize = 3.0f;
	glBegin(GL_QUADS);
	glColor3f(1.0f, 0.0f, 0.0f); //Set color to red
	glVertex2f(-(squareSize/2), squareSize / 2); //(-x,y)
	glVertex2f(squareSize / 2, squareSize / 2); //(x,y)
	glVertex2f((squareSize / 2), -(squareSize / 2)); //(x,-y)
	glVertex2f(-(squareSize / 2), -(squareSize / 2)); //(-x,-y)
	glEnd();

	//Triangle
	glBegin(GL_TRIANGLES);
	glColor3f(1.0f, 1.0f, 0.0f); //Set color to yellow
	glVertex2f(0.0f, 0.75f); //(x,y)
	glVertex2f(0.5f, -0.25f); //(x,-y)
	glVertex2f(-0.5f, -0.25f); //(-x,-y)
	glEnd();

	// Point at center of triangle
	glBegin(GL_LINE_LOOP);
	glColor3f(1.0f, 1.0f, 1.0f); //Set color to white
	int num_segments = 100;
	float cx = 0.0f;
	float cy = 0.2f;
	float r = 0.2f;
	for (int ii = 0; ii < num_segments; ii++) {
		float theta = 2.0f * 3.1415926f * float(ii) / float(num_segments);//get the current angle 
		float x = r * cosf(theta);//calculate the x component 
		float y = r * sinf(theta);//calculate the y component 
		glVertex2f(x + cx, y + cy);//output vertex 
	}
	glEnd();

	glFlush(); //render
}

int main(int argc, char**argv) {
	glutInit(&argc, argv); //Initialize glut
	glutCreateWindow("Square of mine"); // Create window with title
	glutInitWindowSize(500,500); // Window initial window height and width
	glutInitWindowPosition(50, 50); // Init window position to the top left corner
	init();
	glutDisplayFunc(render); // Pass function that renders shape
	glutReshapeFunc(changeViewPort);
	glutMainLoop(); //Enter event processing loop


	return 0;
}*/