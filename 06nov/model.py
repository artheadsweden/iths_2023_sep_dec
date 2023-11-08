import os.path
import torch
from torch import nn, optim
import torch.nn.functional as F


class LinearQNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)

    def forward(self, state_tensor):
        state_tensor = F.relu(self.linear1(state_tensor))
        state_tensor = self.linear2(state_tensor)
        return state_tensor

    def save(self, file_name='model.pth'):
        model_folder_path = './model'
        if not os.path.exists(model_folder_path):
            os.makedirs(model_folder_path)
        file_name = os.path.join(model_folder_path, file_name)
        torch.save(self.state_dict(), file_name)


class QTrainer:
    def __init__(self, model, lr, gamma):
        self.model = model
        self.lr = lr
        self.gamma = gamma

        self.optimizer = optim.Adam(model.parameters(), lr=lr)
        self.criterion = nn.MSELoss()  # Mean Squared Error (Q2 - Q1)^2 = loss

    def train_step(self, state, action, reward, next_state, done):
        state = torch.tensor(state, dtype=torch.float)
        action = torch.tensor(action, dtype=torch.long)
        reward = torch.tensor(reward, dtype=torch.float)
        next_state = torch.tensor(next_state, dtype=torch.float)

        # If we only get values for one step
        if len(state.shape) == 1:
            state = torch.unsqueeze(state, 0)
            action = torch.unsqueeze(action, 0)
            reward = torch.unsqueeze(reward, 0)
            next_state = torch.unsqueeze(next_state, 0)
            done = (done, )

        # 1. Predict Q value with the current state
        pred_q = self.model(state)

        # 2. q_new = reward + gamma * max(next_state)
        target = pred_q.clone()
        for idx in range(len(done)):
            q_new = reward[idx] + self.gamma * torch.max(self.model(next_state[idx])) if not done[idx] else reward[idx]

            target[idx][torch.argmax(action).item()] = q_new

        self.optimizer.zero_grad()
        loss = self.criterion(target, pred_q)

        loss.backward()  # Backpropagation
        self.optimizer.step()



