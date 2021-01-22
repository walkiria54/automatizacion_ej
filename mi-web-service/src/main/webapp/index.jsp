<%@ page language="java" contentType="text/json; charset=UTF-8" 
pageEncoding="UTF-8"%>
<%
int a=Integer.parseInt(request.getParameter("numero1"));
int b=Integer.parseInt(request.getParameter("numero2"));
%>
{
    'resultado' :<%= (a+b) %>
}