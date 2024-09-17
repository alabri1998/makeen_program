const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());

app.post('/chatgpt', async (req, res) => {
    const prompt = req.body.prompt;

    try {
        const response = await axios.post('https://api.openai.com/v1/chat/completions', {
            model: 'gpt-3.5-turbo',
            messages: [{ role: 'user', content: prompt }]
        }, {
            headers: {
                'Authorization': `Bearer sk-vFAp4tzxsMl0EFD2qO9SbGJoDBUjh7umrK-ZA2JSwIT3BlbkFJ5Bwl2p5GvXS6jVmDIvdVjVk8jIYOBcZrRM2N93L74A`,  // Replace with your OpenAI API key
                'Content-Type': 'application/json'
            }
        });

        const completion = response.data.choices[0].message.content;
        res.json({ response: completion });
    } catch (error) {
        console.error('Error with the OpenAI API:', error.response ? error.response.data : error.message);
        res.status(500).json({ error: 'Failed to get a response from the OpenAI API' });
    }
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
