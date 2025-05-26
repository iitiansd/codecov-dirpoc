package com.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class LoggingClientTest {

    @Test
    public void testLogMessageValid() {
        LoggingClient client = new LoggingClient("TestService");
        String result = client.logMessage("Hello, World!");
        assertEquals("[TestService] Hello, World!", result);
    }

    @Test
    public void testLogMessageEmpty() {
        LoggingClient client = new LoggingClient("TestService");
        String result = client.logMessage("");
        assertEquals("Error: Empty or null message", result);
    }

    @Test
    public void testLogMessageNull() {
        LoggingClient client = new LoggingClient("TestService");
        String result = client.logMessage(null);
        assertEquals("Error: Empty or null message", result);
    }

    @Test
    public void testIsValidMessageValid() {
        LoggingClient client = new LoggingClient("TestService");
        assertTrue(client.isValidMessage("Valid message"));
    }

    @Test
    public void testIsValidMessageInvalid() {
        LoggingClient client = new LoggingClient("TestService");
        assertFalse(client.isValidMessage(""));
        assertFalse(client.isValidMessage(null));
    }
}