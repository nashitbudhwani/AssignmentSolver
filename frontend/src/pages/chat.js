import React, { useState } from "react";
import axios from "axios";
import { Typography, Box, Button, TextField, Paper } from "@mui/material";

function Chat({ answer }) {
  const [content, setContent] = useState(answer.text || "");
  const [gptAnswer, setGptAnswer] = useState("");
  const [paraphrasedAnswer, setParaphrasedAnswer] = useState("");
  const [isAnswerEnabled, setIsAnswerEnabled] = useState(false);
  const [isParaphraserEnabled, setIsParaphraserEnabled] = useState(false);

  const chatApi = process.env.REACT_APP_API + "/gpt";
  const pharaphraseApi = process.env.REACT_APP_API + "/paraphrase";

  const handleChatClick = async () => {
    try {
      const uploadResponse = await axios.post(
        chatApi,
        {
          user_message: content,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      console.log("Message sent successfully:", uploadResponse.data);
      setGptAnswer(uploadResponse.data.answer);
      setIsAnswerEnabled(true);
      return uploadResponse.data;
    } catch (error) {
      console.error("Failed to send message!", error);
    }
  };

  const handlePharaphaseClick = async () => {
    try {
      const uploadResponse = await axios.post(
        pharaphraseApi,
        {
          input_text: gptAnswer,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      console.log("Message sent successfully:", uploadResponse.data);
      setParaphrasedAnswer(uploadResponse.data.answer);
      setIsParaphraserEnabled(true);
      return uploadResponse.data;
    } catch (error) {
      console.error("Failed to send message!", error);
    }
  };

  return (
    <Box>
      <Box sx={{ p: 3, mt: "5vh" }}>
        <TextField
          label="Your Message"
          variant="outlined"
          fullWidth
          multiline
          rows={4}
          value={content}
          onChange={(e) => setContent(answer.text + e.target.value)}
        />
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            marginTop: "10px",
          }}
        >
          <Paper sx={{ padding: 2, width: "45%", overflowWrap: "break-word" }}>
            {!isAnswerEnabled && (
              <Typography>
                Search the retrieved text on chat GPT to find an answer
              </Typography>
            )}
            {isAnswerEnabled && <Typography> Answer: {gptAnswer}</Typography>}
          </Paper>
          <Paper sx={{ padding: 2, width: "45%", overflowWrap: "break-word" }}>
            {isParaphraserEnabled && (
              <Typography> Paraphrased: {paraphrasedAnswer}</Typography>
            )}
          </Paper>
        </div>
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            marginTop: "10px",
          }}
        >
          <Button
            variant="contained"
            color="primary"
            onClick={handleChatClick}
          >
            Chat
          </Button>
          <Button
            variant="contained"
            color="primary"
            onClick={handlePharaphaseClick}
          >
            Paraphrase
          </Button>
        </div>
      </Box>
    </Box>
  );
}

export default Chat;
