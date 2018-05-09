import visdom
import torch 

# create an environment
vis = visdom.Visdom(env='env_name')

# text
vis.text('text', win='win_name')
# append
vis.text('append content', win='win_name', append=True)


# line example
for i in range(1000):
    vis.line(X=torch.FloatTensor([i]), Y=torch.FloatTensor([i**2]), win='loss', update='append' if i > 0 else None)
