# Competitive Programming Template

Engineers need to solve problems that they have never seen before efficiently and practically. One needs to practice to master this skill. With this goal in mind, I created this repository to store my solutions and share them with those in need.

**Note:** This repo is a template used by me for organizing my solutions. If you are looking for my solutions instead then click [here](https://github.com/muj-programmer/cp_is_awesome.git)

So without wasting your precious time :clock1130:, Let's set up this template for you.

## Create Your Repository

Well, I'm damn sure you know how to create a remote repository but just for my peace of mind, I will share my steps.

- Login to your **Github Account**.
- Click on _create new repository_, give it a name that you prefer.

And that's all you need to setup this template.

**Note:** Make sure your repository is **public**. You can create your repo on your _preferred git hosting service_.

## Clone Repository

Open your terminal and I think you know what the next move is. (copy-paste the command :open_mouth:)

```bash
git clone https://github.com/muj-programmer/cp_template <your_repo_name>
```

**Note:** `<your_repo_name>` needs to be replaced with the repo name you created previously. (You can however give it any name, but I won't recommend that)

## Visit Your Template

Let's `cd` into your cloned template.

```bash
cd <your_repo_name>
```

## Run the `install` Script

You are almost done :hourglass:, Set up your template with this command

```bash
sh install.sh <remote_url>
```

**Note:** So you remember you created a new repo on your git hosting service, Well now you need to get the _url_ of that and replace it with `<remote_url>`

## How-To-Use

The _setup is complete_ :100:, you should see an __initial commit__ in your _local repo_ as well as _remote repo_.

__3__ new aliases have been created for you :fire: to interact with your template. (_it's placed in your shell config file_)

| alias  | purpose                      |
|--------|------------------------------|
| `csf`  | create new solution file     |
| `psf`  | push changes to remote repo  |
| `rmlf` | remove log files in tool dir |

__Note:__ check out the [wiki](https://github.com/muj-programmer/cp_template/wiki) for a tutorial.

## Commit Emojis

You have probably come across a lot of emojis in the commit history or while browsing the repository and tried to figure out what does it imply.
Well let's put an end to this energy-draining task.

| Emoji              | Markup               | Abbreviation | Purpose                     |
| ------------------ | -------------------- | ------------ | --------------------------- |
| :white_check_mark: | `:white_check_mark:` | AC           | passed all testcases        |
| :x:                | `:x:`                | WA           | fails one or more testcases |
| :exclamation:      | `:exclamation:`      | TLE          | scope for optimization      |
| :question:         | `:question:`         | INC          | incomplete solution         |
|                    |                      | PVT          | private solution            |

**Note:** `PVT` is used to keep the solution untracked in git, ensuring that the solution is not available on GitHub by mistake.

## Facing a Issue

If you are in this situation _first and foremost_ Don't panic :cry: I'm here to help you get over it. Simply click [this](https://github.com/muj-programmer/cp_template/issues) and properly state your issue (be as verbose as you can be), After that sit tight and watch :movie_camera: the movie you have been postponing for so long while I :construction_worker: fix the issue.

## Want to Contribute

I will be glad :smiley: to work with you on a new idea or fixing a invisible bug :bug: or if you have already done the work :hammer: just create a pull request and I will merge it asap.

Well that's all for now but before you close this browser tab hit the star :star: button (it motivates me to make new stuff).

Have a great day :sunglasses:.
