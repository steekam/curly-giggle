///*
//	Admission: 100565
//*/
//
//#define _USE_MATH_DEFINES
//
//#include <Windows.h>
//#include <GL/glut.h>
//#include <math.h>
//
//constexpr auto WINDOW_WIDTH = 800;;
//constexpr auto WINDOW_HEIGHT = 600;;
//
//void init() {
//	glClearColor(1.0f, 1.0f, 1.0f, 1.0f); // set background color to white and opaque
//	gluOrtho2D(-WINDOW_WIDTH/2, WINDOW_WIDTH / 2, -WINDOW_HEIGHT / 2, WINDOW_HEIGHT / 2);
//}
//
//void myArc() {
//	float x = -290.0f;
//	float y = 190.0f;
//	float radius = 100.0f;
//
//	int lineAmount = 100; //# of triangles used to draw circle
//
//	glBegin(GL_LINE_STRIP);
//	glColor3f(0.0f, 0.0f, 0.0f);
//	for (float i = 0; i <= lineAmount;i++) {
//		glVertex2f(
//			x + (radius * (GLfloat)cos(i * M_PI / lineAmount)),
//			y + (radius * (GLfloat)sin(i * M_PI / lineAmount))
//		);
//	}
//	glEnd();
//}
//
//void twoSquares() {
//	float x1 = 60.0f;
//	float y1 = 200.0f;
//	float sidelength = 150.0;
//	float halfside = sidelength / 2;
//
//	glColor3d(0, 0, 0);
//	glBegin(GL_LINE_LOOP);
//	glVertex2f(x1 + halfside, y1 + halfside);
//	glVertex2f(x1 + halfside, y1 - halfside);
//	glVertex2f(x1 - halfside, y1 - halfside);
//	glVertex2f(x1 - halfside, y1 + halfside);
//	glEnd();
//
//	float sidelength2 = 120.0;
//	float halfside2 = sidelength2 / 2;
//	glBegin(GL_LINE_LOOP); //square 2
//	glVertex2f(x1 + halfside2, y1 + halfside2);
//	glVertex2f(x1 + halfside2, y1 - halfside2);
//	glVertex2f(x1 - halfside2, y1 - halfside2);
//	glVertex2f(x1 - halfside2, y1 + halfside2);
//	glEnd();
//}
//
//void myStar() {
//	// Assume equilateral triangle
//	float sidelength = 100.0f;
//	float halfside = sidelength / 2;
//	float centerX = 200.0f;
//	float centerY = 100.0f;
//
//	glBegin(GL_LINE_LOOP); //triangle 1
//	glColor3f(0.5, 0, 0);
//	glVertex2f(centerX + halfside, centerY - halfside);
//	glVertex2f(centerX - halfside, centerY - halfside);
//	glVertex2f(centerX, centerY + halfside);
//	glEnd();
//
//	centerY -= 30.0f ;
//	glBegin(GL_LINE_LOOP); //triangle 2
//	glColor3f(0.5, 0, 0);
//	glVertex2f(centerX + halfside, centerY + halfside);
//	glVertex2f(centerX - halfside, centerY + halfside);
//	glVertex2f(centerX, centerY - halfside);
//	glEnd();
//}
//
//void threeCircles() {
//	float x = -290.0f;
//	float y = -10.0f;
//	float radius = 50.0f;
//
//	int lineAmount = 100; //# of triangles used to draw circle
//	glColor3f(0.0f, 0.0f, 0.0f);
//
//	//circle 1
//	glBegin(GL_LINE_LOOP);
//	for (int i = 0; i <= lineAmount;i++) {
//		glVertex2f(
//			x + (radius * (GLfloat)cos(i * (2 * M_PI) / lineAmount)),
//			y + (radius * (GLfloat)sin(i * (2 * M_PI) / lineAmount))
//		);
//	}
//	glEnd();
//	//circle 2
//	glBegin(GL_LINE_LOOP);
//	x += radius + (radius - 30.0f);
//	for (int i = 0; i <= lineAmount;i++) {
//		glVertex2f(
//			x + (radius * (GLfloat)cos(i * (2 * M_PI) / lineAmount)),
//			y + (radius * (GLfloat)sin(i * (2 * M_PI) / lineAmount))
//		);
//	}
//	glEnd();
//	//circle 3
//	glBegin(GL_LINE_LOOP);
//	x -= radius - (30.0f/2);
//	y += 50.0f;
//	for (int i = 0; i <= lineAmount;i++) {
//		glVertex2f(
//			x + (radius * (GLfloat)cos(i * (2 * M_PI) / lineAmount)),
//			y + (radius * (GLfloat)sin(i * (2 * M_PI) / lineAmount))
//		);
//	}
//	glEnd();
//}
//
//void render() {
//	myArc();
//	twoSquares();
//	myStar();
//	threeCircles();
//	glFlush(); //render
//}
//
//int main(int argc, char** argv) {
//	glutInit(&argc, argv); //Initialize glut
//	glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT); // Window initial window height and width
//	glutInitWindowPosition(10, 50); // Init window position to the top left corner
//	glutCreateWindow("Preliminary Lab"); // Create window with title
//	init();
//	glutDisplayFunc(render); // Pass function that renders shape
//	glutMainLoop(); //Enter event processing loop
//
//	return 0;
//}