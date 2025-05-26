package com.example;

public class LoggingClient {
    private String serviceName;

    public LoggingClient(String serviceName) {
        this.serviceName = serviceName;
    }

    public String logMessage(String message) {
        if (message == null || message.isEmpty()) {
            return "Error: Empty or null message";
        }
        return "[" + serviceName + "] " + message;
    }

    public boolean isValidMessage(String message) {
        return message != null && !message.trim().isEmpty();
    }
}