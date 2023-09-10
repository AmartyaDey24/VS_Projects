package com.practice;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class AddServlet extends HttpServlet{

    public void doPost(HttpServletRequest req, HttpServletResponse res){

        int num1 = Integer.parseInt(req.getParameter("num1"));
        int num2 = Integer.parseInt(req.getParameter("num2"));

        int result = num1 + num2;

        try {
            PrintWriter out = res.getWriter();
            out.println("The result is: " + result);
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
    
}
